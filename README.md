# Hotel Revenue & Occupancy Analytics

## 1. Project Overview
This project analyses historical hotel booking data to understand booking patterns, cancellation behaviour, and average daily room rates. An interactive dashboard was developed using Python and Streamlit to present the findings.

## 2. Problem Statement
Hotels need to understand booking patterns and cancellations to support operational planning and improve booking management. This project explores historical hotel booking records to identify trends and differences between hotel types.

## 3. Objectives
- Analyse booking records by hotel type and arrival month.
- Calculate and compare cancellation rates.
- Examine average daily room rates.
- Present findings through an interactive dashboard.
- Provide data-based recommendations for hotel management.

## 4. Dataset
**Dataset:** Hotel Booking Demand Dataset

**Original research source:** António, N., de Almeida, A., and Nunes, L. (2019), *Hotel Booking Demand Datasets*, Data in Brief.

**Publication link:** https://doi.org/10.1016/j.dib.2018.11.126

**CSV used:** https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-02-11/hotels.csv

The dataset contains 119,390 records and 32 columns, including hotel type, cancellation status, arrival dates, booking channels, and average daily room rate.

## 5. Tools and Technologies
- Python
- Pandas
- Plotly
- Streamlit
- GitHub

## 6. Methodology
1. Load the public hotel booking dataset.
2. Inspect the dataset structure, missing values, and duplicate records.
3. Handle missing values in selected categorical columns.
4. Calculate booking counts, cancellation rates, and average daily room rates.
5. Analyse monthly booking patterns and differences between hotel types.
6. Develop an interactive dashboard with filters and visualisations.

## 7. Key Findings
- The dataset contains 119,390 booking records.
- The overall cancellation rate is approximately 37.04%.
- City Hotel records have a cancellation rate of approximately 41.73%.
- Resort Hotel records have a cancellation rate of approximately 27.76%.
- August has the highest monthly booking count in the combined dataset, while January has the lowest.

## 8. Dashboard Features
- Booking record and cancellation KPIs.
- Hotel type and arrival year filters.
- Monthly booking trend chart.
- Hotel type comparison.
- Cancellation rate visualisation.
- Average daily room rate analysis.

## 9. Business Recommendations
- Investigate the higher cancellation rate among City Hotel bookings.
- Review booking channels and lead times to understand cancellation patterns.
- Use monthly booking trends to support staffing and promotional planning.
- Review room rate patterns when planning pricing strategies.

## 10. Limitations
The dataset contains historical booking records rather than verified financial statements. Average daily room rates are not equivalent to actual recognised revenue, and exact hotel occupancy cannot be established without information about room availability. Duplicate records were identified and retained for review rather than automatically deleted.

## 11. Live Dashboard
https://hotel-revenue-analytics-kdvlxg8b9smmhrtcd9354n.streamlit.app/

## 12. Conclusion
This project demonstrates how Python-based data analysis and an interactive Streamlit dashboard can help identify hotel booking patterns, cancellation behaviour, and differences in room rates. The findings can support further investigation and data-informed operational decisions.

## 13. References
1. António, N., de Almeida, A., and Nunes, L. (2019). Hotel Booking Demand Datasets. Data in Brief. https://doi.org/10.1016/j.dib.2018.11.126
2. Hotel Booking Dataset CSV: https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-02-11/hotels.csv
