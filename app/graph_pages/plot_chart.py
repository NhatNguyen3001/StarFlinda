import altair as alt
from matplotlib.pyplot import scatter, title, ylim
from numpy import size
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Plot chart")
    with st.container():
        st.write("""StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.

                    Guide
                    Step 1) Please choose one of the data types on the select box.
                    Step 2) Check out a beautiful pie chart StaFiIndia provide.
                    Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.
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