import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from PIL import Image

st.title("Line Graph")

# LOAD DATA

eco = pd.read_csv('eco.csv')
bus = pd.read_csv('business.csv')

# SELECTION
airline = eco['airline'].unique().tolist()
price = eco['price'].unique().tolist()

price_selection = st.slider('Price: ',
                            min_value=min(price),
                            max_value=max(price),
                            value=(min(price), max(price)))

airline_selection = st.multiselect('Airline: ',
                                   airline,
                                   default=airline)

# FILTER DATAFRAME
mask = (eco['price'].between(*price_selection)) & (eco['airline'].isin(airline_selection))
number_of_result = eco[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# GRAPH
chart = alt.Chart(eco, title="Economy Class").mark_line().encode(
    x='ticket_id',
    y='price'
)

chart2 = alt.Chart(bus, title="Business Class").mark_line().encode(
    x='ticket_id',
    y='price'
)

st.altair_chart(chart, use_container_width=True)
st.altair_chart(chart2, use_container_width=True)

st.write(eco)
st.write(bus)
