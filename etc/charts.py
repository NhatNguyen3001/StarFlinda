import streamlit as st
import pandas as pd
import altair as alt


# Hide menu
hide_menu = """
<style>
#MainMenu { visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title("CHARTS")

# Link css footer
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

# Sidebar
##Button css
buttoncss = st.markdown("""
<style>
div.stButton > button:first-child {
    width:705px;
    height:50px;
    justify-content: left;
    font-family: "IBM Plex Sans", sans-serif;
    font-size: 0.8rem;
}
</style>""", unsafe_allow_html=True)

#Function
##CSV file
csv_url = 'https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data.csv'
df = pd.read_csv(csv_url)

###Price_bar
pricechart = alt.Chart(df).mark_bar().encode(
    y=alt.Y('count(airline):O', title="Number of flight"),
    x=alt.X('class:N', title="Class"),
    color='class:N',
    column='airline:N'
).properties(height=500, width=85)

##Price button
price_chart = st.button("Price")

if price_chart:
    st.altair_chart(pricechart)

## Duration
d_expander = st.expander("Duration")
departure = d_expander.selectbox(
    'Select your departure',
    ('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Mumbai', 'Kolkata'))
destination = d_expander.selectbox(
    'Select your destination',
    ('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Mumbai', 'Kolkata'))
duration = d_expander.slider(
    'Select your duration',
    min_value=2150, max_value=93200, step=1)

##Class
c_expander = st.button("Class")

##Flight Map
fm_expander = st.expander("Flight Map")
choose = fm_expander.radio(
    "Select kind of map you wanna see",
    ('Departure', 'Destination'))

# Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
<div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
</nav>
""", unsafe_allow_html=True)
