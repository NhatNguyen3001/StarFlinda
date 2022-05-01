import streamlit as st
import pandas as pd
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px

st.title("graph")

# LOAD DATA

df = pd.read_csv('data.csv')
df.columns = ['date', 'airline', 'ch_code', 'num_code', 'dep_time', 'from', 'time_taken', 'stop', 'arr_time', 'to', 'price', 'class', 'ticket_id', 'weekday']
price = df['price'].unique().tolist()
airline = df['airline'].unique().tolist()
flight_class = df['class'].unique().tolist()
from_des = df['from'].unique().tolist()

st.write(df)

start_price = st.selectbox('Start Price: ', price, 0)
end_price = st.selectbox('End Price: ', price, 0)
airline_options = st.multiselect('Airline: ', airline, default=airline)
class_options = st.multiselect('Class: ', flight_class, default=flight_class)

df = df[df['airline'].isin(airline_options)]
df = df[df['price'] >= start_price]
df = df[df['price'] <= end_price]
df = df[df['class'].isin(class_options)]

x = df['airline']
y = df['price']

fig = alt.Chart(df).mark_bar().encode(
     x="airline", y="price", color="airline").interactive()

st.altair_chart(fig, use_container_width=True)
