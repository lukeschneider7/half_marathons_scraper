## half_marathons_scraper purpose

   Running is something I've always had a passion for and after having the time of my life running the Shamrock Half Marathon in Virginia Beach last year I've been looking for my next race. As such I thought I would make a tool for helping me find possible races around Virginia to train for. 

## Overview

   This project involves extracting and visualizing upcoming half marathons [running in the usa site](https://runningintheusa.com/classic/list/within-200-miles-of-virginia%20beach-va/upcoming/half-marathon/miles-between-250/page-2) within 200 miles of Virginia Beach, VA, using Python. The project utilizes web scraping techniques with the **BeautifulSoup** library and performs data analysis using **Pandas** and **Plotly** for visualization. Ongoing project work is to develop a streamlit dashborad based on customizable user generated parameters such as what distance someone wants to run, as well as date range, and distance from them to show them race options for.


[View Jupyter Notebook Results](https://lukeschneider7.github.io/half_marathons_scraper/half_marathons.html)

## Project details

1. **Web Scraping**:
   - Extracts race titles, dates, and cities from the Running in the USA website.
3. **Data Processing**:
   - Converts race dates to datetime objects, adds a day of the week column, and organizes the data into a DataFrame.
   - Export: saves the processes data to a CSV file.
4. **Data Analysis**:
   - Counts of half marathons by city
   - Summary table of all races
   - Counts of races occurring on each date
5. **Visualization**:
   - Interactive bar plots showing counts of races by day of the week and month

## In progress
5. **Streamlit UI dashboard for customized race scraping** 
   - generate dashboard with UI taking parameters of user city, race type, date range, and distance from user (radial) to scrape running the    usa website and give user .csv file of races along with vizualizations of available races
