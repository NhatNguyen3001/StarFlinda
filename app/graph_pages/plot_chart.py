import altair as alt
from matplotlib.pyplot import scatter, title, ylim
matplotlib.use('Agg')
from numpy import size
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Plot chart")
    with st.container():
        st.write("""
                    StaFiIdia provides a data comparison service for two tickets' information.
                    It enables users to see details of the ticket and compare two tickets by each element.
                    """)
        st.header("Guide")
        st.write("""
                Step 1) Put the first ticket id and the second ticket id on the input box.\n
                Step 2) Click the submit button.\n
                Step 3) See the result.
                """)


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

    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)