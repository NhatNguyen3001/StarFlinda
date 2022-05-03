import altair as alt
from matplotlib.pyplot import scatter, title, ylim
from numpy import size
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    csv_url ='https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data.csv'
    df = pd.read_csv(csv_url)
    d = st.selectbox("Pie chart about:",
                                ('Air India', 'AirAsia', 'GO FIRST', 'Indigo', 'SpiceJet',
                                'Vistara'))


    scatter = alt.Chart(df ).mark_point(filled=True).encode(
        alt.X('dep_time'),
        alt.Y('price'),
        alt.Size('class', scale=alt.Scale(range=[200, 500])),
        alt.OpacityValue(0.6),
        alt.Color('class'),
        tooltip = ['date', 'ch_code', 'from', 'to']
    ).transform_filter(alt.FieldEqualPredicate(field='airline', equal=d)).properties(height=850, width=850, title = 'Plot chart').interactive()
    
    st.altair_chart(scatter)