import streamlit as st
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import json
import time 

st.title('Race Finder')
st.markdown('### See first 40 races given parameters below')

crawl_delay = 15
r = requests.get('https://httpbin.org/user-agent')
useragent = json.loads(r.text)['user-agent']
headers = {'User-Agent': useragent,
           'from': 'vrd9sd@virginia.edu'}

st.text_input("Your City (ex. Virginia Beach)", key="city")
st.text_input("Your State (ex. va)", key="state")
st.text_input("distance? (5k, 10k, half-marathon, marathon)", key="distance")
st.text_input("Races within how many miles from you? (25, 50, 100, 200)", key="location")
#race_distance = st.sidebar.selectbox(
   # 'What distance are you looking to race?',
    #('5k', '10k', 'half-marathon', 'marathon')#)
#location = str(st.sidebar.selectbox(
    #'Races within how many miles of you?',
    #('25', '50', '100', '200')#))

# You can access the value at any point with:
city = st.session_state.city
state = st.session_state.state
race_distance = st.session_state.distance
location = st.session_state.location

url = "https://halfmarathonsscraper-qymaruem5etv6hyorcncz6.streamlit.app/"
if location:
    url = f"https://runningintheusa.com/classic/list/within-{location}-miles-of-{city.replace(' ', '%20')}-{state}/upcoming/{race_distance}/miles-between-250/page-1"
    st.write(url)
else:
    st.write("Please enter a valid location distance.")

r = requests.get(url, headers=headers)
# Parsing HTML code 
mysoup = BeautifulSoup(r.text, 'html.parser')

# part 1B: function to scrape races from the running in the usa website
def race_df(url):
    """ function for returning df w/ race info given a url
    Args:
        url: (str) a string of a race 
    Returns:
        races: (df) a DataFrame containg race dates, titles, cities
    """

    r = requests.get(url, headers=headers)
    mysoup = BeautifulSoup(r.text, 'html.parser')
 
    titles = [x.b for x in mysoup.find_all('td', attrs = {'style': 'text-decoration:inherit;'})]
    titles = [x.string for i, x in enumerate(titles) if i%2==1]

    rowspan_1_2_cities = [x.b for x in mysoup.find_all('td', attrs={'rowspan':['1', '2']})]
    cities = rowspan_1_2_cities[2:]
    cities = [x.string for i,x in enumerate(cities) if i%4==0] #and i > 7]

    dates = [x.string for x in mysoup.find_all('div', attrs = {'style':"font-weight:bold"})]
    dates = [x for i,x in enumerate(dates) if i>1 and i<= (len(cities) + 1)]

    distances = [x.string for x in mysoup.find_all('div', attrs={'style':"padding-left:10px"}) if x.string and (x.string.endswith('run') or x.string.endswith('relay'))]
   
    if len(dates) == len(titles) == len(cities) ==len(distances): # ensure I am getting each record (lenths should be the same)
        # Part 1D: Makes races df, use indexing to feature out featured listings at top
        races = pd.DataFrame({
        'date' : dates[2:], 
        'race': titles[2:],
        'city': cities[2:], 
        'distance': distances[2:]})
    else:
        races = -1 
    return races


# Only scraper if all parameters are filled out!
if location and city and state and race_distance:
    new_df = race_df(url)
    # Part 1C: Turn this web-scraper into a spider!
    for i in range(2, 3):
        url = url[:-1] + str(i) # Insert new number into url str for pages 2-6
        new_df = pd.concat([new_df, race_df(url)], ignore_index=True) # use scraping function as spider
        time.sleep(crawl_delay) # delay to not get banned 
    
    new_df['date'] = pd.to_datetime(new_df.date) # Convert date column to datetime
    new_df['day'] = new_df['date'].dt.day_name() # Add day of week column
    new_df = new_df[['day', 'date', 'race', 'city', 'distance']] # Order columns in DF to be more readable
    new_df = new_df.sort_values(by='date', ascending=True) # Sort by date

    city_race_count = new_df.groupby(['city']).agg({'race':'count'}).sort_values(by='race', ascending=False)   
    city_race_count = city_race_count.reset_index(drop=False).rename({'city': 'city'}, axis=1)
    st.write("Number of Races by city:")
    st.dataframe( city_race_count[0:5])

    st.write("Races not on weekends:")
    weekday_races = new_df.query("day != 'Saturday' & day!= 'Sunday'")
    st.dataframe(weekday_races)
    
    st.write("all_races")
    st.dataframe(new_df)

 

