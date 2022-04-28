from numpy import char
import streamlit as st
from app import compare_tickets, contact_us, homepage, search2
from app.graph_pages import table, line_chart, charts2, piechart
from streamlit_option_menu import option_menu


#build webpage


# REF : https://github.com/insightsbees/streamlit_app_gallery/blob/main/streamlit_app_gallary.py

# SET NAVIGATION BAR
with st.sidebar:
    choose = option_menu("Menu", ["HOME", "DATA SEARCH", 
                                    "ㄴTable", "ㄴLine chart", "ㄴBar chart", "ㄴPie chart", "ㄴMap", 
                                    "DATA COMPARISION", "CONTACT US"],
                         icons=['house', 'search', 
                                'bar chart', 'bar chart', 'bar chart', 'bar chart', 'bar chart', 
                                'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                            "container": {"padding": "5!important", "background-color": "black"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#02ab21"},
                        }
    )

if choose == "HOME":
    homepage.app()
elif choose == "DATA SEARCH":
    search2.app()
#grach pages 
elif choose ==  "ㄴTable":
    table.app()
elif choose ==  "ㄴLine chart":
    table.app()
elif choose ==  "ㄴBar chart":
    charts2.app()
elif choose ==  "ㄴPie chart":
    piechart.app()
elif choose ==  "ㄴMap":
    compare_tickets.app()
elif choose == "DATA COMPARISION":
    compare_tickets.app()
elif choose == "CONTACT US":
    contact_us.app()
    