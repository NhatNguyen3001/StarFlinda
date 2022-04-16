import streamlit as st
import pandas as pd
from PIL import Image

# Hide menu
hide_menu = """
<style>
#MainMenu { visibility: hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

#Image embed
image = Image.open('1.jpg')
st.image(image)

#Navigation bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #234362; border-bottom-style: solid;">
  <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/277853292_693501878552093_5397392246607986926_n.png?stp=dst-png_p403x403&_nc_cat=103&ccb=1-5&_nc_sid=aee45a&_nc_ohc=CRZgymqdYmoAX_Oh50H&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVIYtVzGEF4Z_YFfP-wVmrRDe2QNdBfMyfqSo-BIFboqnA&oe=62820FB1" 
            class="rounded float-left" alt="MAFOOD" width="50" height="50">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank" style="color: #FFFFFF;">STAFLINDA</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse " id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#" style="color: #FFFFFF;"> Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank" style="color: #FFFFFF;">Cuisine</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #FFFFFF;">Category</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #FFFFFF;">Location</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #FFFFFF;">Reccomendation</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#Searching fligh box
Departure, Destination = st.columns(2)
Departure.selectbox(
     'Choose your departure of the flight?',
     ('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Mumbai', 'Kolkata'))
Destination.selectbox(
     'Choose your flight destination?',
     ('Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Mumbai', 'Kolkata'))
Search_button= st.button('SEARCH FLIGHT')

#flight_static_table + chart
flight_static_table = st.container()
chart = st.container()

#chart
chart.PRICE, chart.ClASS = st.columns(2)

chart.PRICE.image(image)
chart.PRICE.write("PRICE")

chart.ClASS.image(image)
chart.ClASS.write("CLASS")

chart.DURATION, chart.FLIGHT_MAP = st.columns(2)

chart.DURATION.image(image)
chart.DURATION.write("DURATION")

chart.FLIGHT_MAP.image(image)
chart.FLIGHT_MAP.write("FLIGHT_MAP")


#flight_static_table
flight_static_table.image(image)
flight_static_table.write("FLIGHT STATIC TABLE")

#Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
  <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
</nav>
""", unsafe_allow_html=True)