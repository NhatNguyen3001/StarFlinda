import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import altair as alt
import plotly.express as px
from PIL import Image

def app():

    st.title("Table")
    st.write("View all the flights information.")
    # LOAD DATA

    data = pd.read_csv("lib//data//data.csv", index_col=0)

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=True,
        height=500,
        width=1000,
        reload_data=True
    )

    data = grid_response['data']
    selected = grid_response['selected_rows']
    df = pd.DataFrame(selected)
    
    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)
