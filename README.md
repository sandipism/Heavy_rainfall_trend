# Heavy_rainfall_trend
Monsoon Onset Trend Analysis for Nepal This project analyzes the monsoon onset dates across multiple locations in Nepal using historical daily rainfall data. It identifies onset dates based on user-defined rainfall thresholds and consecutive days, then visualizes trends interactively with Plotly.
Features
Calculates monsoon onset date for each year based on rainfall threshold and consecutive rainy days.

Supports multiple locations via CSV files.

Converts day-of-year (DOY) to calendar dates.

Interactive Plotly visualization with toggle buttons to compare locations.

Easy to extend with additional rainfall stations or customize onset conditions.

Getting Started
Prerequisites
Python 3.7+

pandas

plotly

Install dependencies using:

bash
Copy
Edit
pip install pandas plotly
Data Format
Place your CSV files inside a folder (e.g., rainfall_data/) with each file named by location (e.g., kathmandu.csv). Each CSV should have these columns:

YEAR	DOY	PRECTOTCORR
2020	1	0.23
2020	2	0.00
...	...	...

YEAR: Year of observation (e.g., 2020)

DOY: Day of year (1 to 365/366)

PRECTOTCORR: Corrected total precipitation in mm for that day

Usage
Run the script:

bash
Copy
Edit
python monsoon_onset_analysis.py
The script:

Reads all CSV files in the specified folder.

Computes the monsoon onset date for each year and location.

Displays an interactive Plotly plot showing onset trends with toggleable location lines.

Customization
Change rainfall threshold and consecutive days by modifying variables in the script:

python
Copy
Edit
threshold = 10  # mm
consecutive_days = 3
Add more stations by adding CSV files to the folder.


