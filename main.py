import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
from apps import about_us, compare_tickets, contact_us
st.set_page_config(page_title="Sharone's Streamlit App Gallery", page_icon="", layout="wide")

# REF : https://github.com/insightsbees/streamlit_app_gallery/blob/main/streamlit_app_gallary.py

# SET NAVIGATION BAR
with st.sidebar:
    choose = option_menu("App Gallery", ["HOME", "DATA SEARCH", "DATA COMPARISION", "ABOUT US", "CONTACT US"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "HOME":
    compare_tickets.app()
elif choose == "DATA SEARCH":
    compare_tickets.app()
elif choose == "DATA COMPARISION":
    compare_tickets.app()
elif choose == "ABOUT US":
    about_us.app()
elif choose == "CONTACT US":
    contact_us.app()