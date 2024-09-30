# marathons_scraper
## Overview

This Jupyter Notebook scrapes upcoming half marathon race data within 200 miles of Virginia Beach, VA, using Python. The project utilizes web scraping techniques with the **BeautifulSoup** library and performs data analysis using **Pandas** and **Plotly** for visualization.

[View Jupyter Notebook Results](half_marathons.html)

## Contents

1. **Web Scraping**: Extracts race titles, dates, and cities from the Running in the USA website.
2. **Data Processing**: Converts race dates to datetime objects, adds a day of the week column, and organizes the data into a DataFrame.
3. **Data Analysis**:
   - Counts of half marathons by city
   - Summary table of all races
   - Counts of races occurring on each date
4. **Visualization**:
   - Interactive bar plots showing counts of races by day of the week and month
5. **Export**: Saves the processed data to a CSV file.
