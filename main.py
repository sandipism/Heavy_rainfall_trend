import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

# === CONFIGURATION ===
folder = 'rainfall_data'  # Folder with multiple location CSVs
threshold = 10  # mm
consecutive_days = 3  # Consecutive days threshold

location_data = {}

# === FUNCTION TO ANALYZE MONSOON ONSET ===
def analyze_onset(file_path):
    df = pd.read_csv(file_path)
    df = df.sort_values(by=['YEAR', 'DOY'])

    onset_dates = []
    for year in df['YEAR'].unique():
        yearly = df[df['YEAR'] == year].reset_index(drop=True)
        rolling_sum = yearly['PRECTOTCORR'].rolling(window=consecutive_days).sum()

        for i in range(len(rolling_sum)):
            if rolling_sum[i] >= threshold * consecutive_days:
                onset_doy = yearly.loc[i, 'DOY']
                onset_dates.append({'YEAR': year, 'DOY': onset_doy})
                break

    if not onset_dates:
        return None, None, None

    onset_df = pd.DataFrame(onset_dates)
    X = onset_df['YEAR'].values.reshape(-1, 1)
    y = onset_df['DOY'].values
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)

    return onset_df, model, y_pred

# === PROCESS EACH FILE ===
for filename in os.listdir(folder):
    if filename.endswith('.csv'):
        location = filename.replace('.csv', '').capitalize()
        filepath = os.path.join(folder, filename)

        onset_df, model, y_pred = analyze_onset(filepath)

        if onset_df is not None:
            location_data[location] = {
                'years': onset_df['YEAR'].values,
                'doys': onset_df['DOY'].values,
                'trend': y_pred,
                'slope': model.coef_[0],
                'mean_onset': np.mean(onset_df['DOY'])
            }

# === PLOTLY INTERACTIVE PLOT ===
fig = go.Figure()

for location, data in location_data.items():
    fig.add_trace(go.Scatter(
        x=data['years'],
        y=data['doys'],
        mode='lines+markers',
        name=f'{location} Onset',
        hovertemplate=f'Year: %{{x}}<br>DOY: %{{y}}<extra>{location}</extra>'

    ))

    fig.add_trace(go.Scatter(
        x=data['years'],
        y=data['trend'],
        mode='lines',
        name=f'{location} Trend (slope={data["slope"]:.2f})',
        line=dict(dash='dash'),
        hoverinfo='skip'
    ))

fig.update_layout(
    title='🌧️ Comparative Heavy Rainfall Onset Trends ',
    xaxis_title='Year',
    yaxis_title='Day of Year (Heavy Rainfall Onset)',
    legend_title='Location',
    hovermode='x unified',
    template='plotly_white'
)

fig.show()
