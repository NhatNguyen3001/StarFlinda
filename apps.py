from numpy import char
import streamlit as st
from app import compare_tickets, contact_us
from streamlit_option_menu import option_menu




#build webpage
st.set_page_config(page_title="StaFiIndia", page_icon="✈️", layout="wide")

# REF : https://github.com/insightsbees/streamlit_app_gallery/blob/main/streamlit_app_gallary.py

# SET NAVIGATION BAR
with st.sidebar:
    choose = option_menu("Menu", ["HOME", "ㄴGraph type 0", "ㄴGraph type 2", "ㄴGraph type 3", "ㄴGraph type 4", "ㄴGraph type 5"
                                        , "DATA SEARCH", "DATA COMPARISION", "CONTACT US"],
                         icons=['house', 'bar chart', 'bar chart', 'bar chart', 'bar chart', 'bar chart',
                                'search', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                            "container": {"padding": "5!important", "background-color": "black"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#02ab21"},
                        }
    )

if choose == "HOME":
    #code for home page
    compare_tickets.app() #delete
elif choose == "DATA SEARCH":
    compare_tickets.app()
#grach pages 
elif choose ==  "ㄴGraph type 1":
    compare_tickets.app()
elif choose ==  "ㄴGraph type 2":
    compare_tickets.app()
elif choose ==  "ㄴGraph type 3":
    compare_tickets.app()
elif choose ==  "ㄴGraph type 4":
    compare_tickets.app()
elif choose ==  "ㄴGraph type 5":
    compare_tickets.app()
elif choose == "DATA COMPARISION":
    compare_tickets.app()
elif choose == "CONTACT US":
    contact_us.app()
    