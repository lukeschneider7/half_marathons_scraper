## half_marathons_scraper purpose

   Running is something I've always had a passion for and after having the time of my life running the Shamrock Half Marathon in Virginia Beach last year I've been looking for my next race. As such I thought I would make a tool for helping me find possible races around Virginia to train for. 

## Overview

   This project involves extracting and visualizing upcoming half marathons [running in the usa site](https://lukeschneider7.github.io/half_marathons_scraper/half_marathons_scraper.html) within 200 miles of Virginia Beach, VA, using Python. The project utilizes web scraping techniques with the **BeautifulSoup** library and performs data analysis using **Pandas** and **Plotly** for visualization. Ongoing project work is to develop a streamlit dashborad based on customizable user generated parameters such as what distance someone wants to run, as well as date range, and distance from them to show them race options for.


[View Jupyter Notebook Results](https://lukeschneider7.github.io/half_marathons_scraper/half_marathons_scraper.html)

## Project details

1. **Web Scraping**: Extracts race titles, dates, and cities from the Running in the USA website.
2. **Data Processing**: Converts race dates to datetime objects, adds a day of the week column, and organizes the data into a DataFrame.
3. **Data Analysis**:
   - Counts of half marathons by city
   - Summary table of all races
   - Counts of races occurring on each date
4. **Visualization**:
   - Interactive bar plots showing counts of races by day of the week and month
5. **Export**: Saves the processed data to a CSV file.

## In progress
**Streamlit UI dashboard for customized race scraping** 
- generate dashboard with UI taking parameters of user city, race type, date range, and distance from user (radial) to scrape running the usa website and give user .csv file of races along with vizualizations of available races
