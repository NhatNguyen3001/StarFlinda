from numpy import char
import streamlit as st
from app import compare_tickets, contact_us, homepage, search2
from app.graph_pages import table, bar_chart, pie_chart, map
from streamlit_option_menu import option_menu

#build webpage
st.set_page_config(layout="wide")

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}<\style>',unsafe_allow_html=True)


# REF : https://github.com/insightsbees/streamlit_app_gallery/blob/main/streamlit_app_gallary.py

# SET NAVIGATION BAR
with st.sidebar:
    choose = option_menu("Menu", ["HOME", "DATA SEARCH", 
                                    "ㄴTable", "ㄴBar chart", "ㄴPie chart", "ㄴPlot chart", "ㄴMap", 
                                    "DATA COMPARISION", "CONTACT US"],
                         icons=['house', 'search', 
                                'bar chart', 'bar chart', 'bar chart', 'bar chart', 'bar chart', 
                                'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                            "container": {"padding": "5!important", "background-color": "#234362!important"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "#FFFFFF"},
                            "nav-link-selected": {"background-color": "#FFFFFF", "color": "#234362"},
                        }
    )

if choose == "HOME":
    homepage.app()
elif choose == "DATA SEARCH":
    search2.app()
#grach pages 
elif choose ==  "ㄴTable":
    table.app()
elif choose ==  "ㄴBar chart":
    bar_chart.app()
elif choose ==  "ㄴPie chart":
    pie_chart.app()
elif choose ==  "ㄴPlot chart":
    table.app()
elif choose ==  "ㄴMap":
    map.app()
elif choose == "DATA COMPARISION":
    compare_tickets.app()
elif choose == "CONTACT US":
    contact_us.app()
    