import streamlit as st
import pandas as pd
import altair as alt
from turtle import title
import matplotlib.pyplot as plt

<<<<<<< Updated upstream:apps/graph_pages/charts.py
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
# Button css
buttoncss = st.markdown("""
<style>
div.stButton > button:first-child {
    width:700px;
    height:50px;
    justify-content: left;
    font-family: "IBM Plex Sans", sans-serif;
    font-size: 0.8rem;
}
</style>""", unsafe_allow_html=True)

# Function
# CSV file
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

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Vistara', 'SpiceJet', 'Indigo', 'GO FIRST', 'Air India', 'AirAsia'
sizes = [42.5, 1.3, 9.6, 13.5, 30.2, 2.9]
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
         startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Economy Class')


labels2 = 'Vistara', 'Air India'
sizes2 = [54.2, 45.8]

fig2, ax2 = plt.subplots()
ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title('Business Class')

##Class
pie_chart = st.button("Class")

if pie_chart:
    economy = st.checkbox("Economy")
    business = st.checkbox("Business")
    if economy:
        st.pyplot(fig1)
    else:
        st.pyplot(fig2)

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
=======
def app():
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
    # Button css
    buttoncss = st.markdown("""
    <style>
    div.stButton > button:first-child {
        width:700px;
        height:50px;
        justify-content: left;
        font-family: "IBM Plex Sans", sans-serif;
        font-size: 0.8rem;
    }
    </style>""", unsafe_allow_html=True)

    # Function
    # CSV file
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

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Vistara', 'SpiceJet', 'Indigo', 'GO FIRST', 'Air India', 'AirAsia'
    sizes = [42.5, 1.3, 9.6, 13.5, 30.2, 2.9]
    explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Economy Class')


    labels2 = 'Vistara', 'Air India'
    sizes2 = [54.2, 45.8]

    fig2, ax2 = plt.subplots()
    ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    ax2.set_title('Business Class')

    ##Class
    pie_chart = st.button("Class")

    if pie_chart:
        economy = st.checkbox("Economy")
        business = st.checkbox("Business")
        if economy:
            st.pyplot(fig1)
        else:
            st.pyplot(fig2)

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
>>>>>>> Stashed changes:app/graph_pages/charts2.py

