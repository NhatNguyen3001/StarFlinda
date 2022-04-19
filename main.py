import streamlit as st
from apps import about_us, compare_tickets, contact_us
st.set_page_config(layout="wide")

# SETTINGS
#variables
HOME = 1
DATA_SEARCH = 2
COMPARE_TICKETS = 3
ABOUT_US = 4
CONTACT_US = 5
set_page = 1 # show HOME page as default

#functions 


# WEB SITE 

nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
with nav_col1:
    if st.button("HOME"):
        set_page = HOME
with nav_col2:
    if st.button("DATA SEARCH"):
        set_page = DATA_SEARCH
with nav_col3:
    if st.button("COMPARE TICKETS"):
        set_page = COMPARE_TICKETS
with nav_col4:
    if st.button("ABOUT US"):
        set_page = ABOUT_US
with nav_col5:
    if st.button("CONTACT US"):
        set_page = CONTACT_US

# apply css file
with open('lib/style/main_style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)


# set page
if (set_page == HOME):
    about_us.app()
elif (set_page == DATA_SEARCH):
    about_us.app()
elif (set_page == COMPARE_TICKETS):
    compare_tickets.app()
elif (set_page == ABOUT_US):
    about_us.app()
elif (set_page == CONTACT_US):
    contact_us.app()

