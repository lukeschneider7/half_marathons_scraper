import streamlit as st
import numpy as np
import pandas as pd








st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))


x = st.slider('lat', -80, 80)  # this is a widget
y = st.slider('lon', -170, 170)
st.write(x, 'is the latitude chosen')


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [2, 2] + [x, y],
    columns=['lat', 'lon'])

st.map(map_data)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name