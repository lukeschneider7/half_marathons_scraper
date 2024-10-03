import streamlit as st
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import json


r = requests.get('https://httpbin.org/user-agent')
useragent = json.loads(r.text)['user-agent']
headers = {'User-Agent': useragent,
           'from': 'vrd9sd@virginia.edu'}

st.text_input("Your City", key="city")
st.text_input("distance? (5k, 10k, half, marathon)", key="distance")
st.text_input("Races within how many miles from you? (25, 50, 100, 200)", key="location")

# You can access the value at any point with:
st.session_state.city
st.session_state.distance
st.session_state.location