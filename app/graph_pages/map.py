import streamlit as st
from streamlit_folium import folium_static
import folium

def app():
    st.title("Map")
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
    with st.container():
        class_to_view = st.selectbox("Choose a class", 
                                    ("Business", "Economy"))

    if class_to_view == "Economy":
        m = folium.Map(location=[22.465609, 80.226926], zoom_start=5)

        folium.Marker(
            [12.971599, 77.594566], popup="Departure: Bangalore", tooltip="Bangalore"
        ).add_to(m)
        folium.Marker(
            [19.075983, 72.877655], popup="Destination: Mumbai", tooltip="Mumbai"
        ).add_to(m)

        folium_static(m, 1000, 714)

    if class_to_view == "Business":
        m = folium.Map(location=[22.465609, 80.226926], zoom_start=4)

        folium.Marker(
            [28.704060, 77.102493], popup="Departure & Destination:\n Delhi", tooltip="Delhi"
        ).add_to(m)
        folium.Marker(
            [19.075983, 72.877655], popup="Destination:\n Mumbai", tooltip="Mumbai"
        ).add_to(m)
        folium.Marker(
            [26.299090, 83.469310], popup="Departure:\n Kokalta", tooltip="Kokalta"
        ).add_to(m)
        folium.Marker(
            [13.082680, 80.270721], popup="Departure & Destination:\n Chennai", tooltip="Chennai"
        ).add_to(m)
        folium.Marker(
            [12.971599, 77.594566], popup="Departure: Bangalore", tooltip="Bangalore"
        ).add_to(m)
        folium.Marker(
            [17.385044, 78.486671], popup="Departure: Hyderabad", tooltip="Hyderabad"
        ).add_to(m)

        folium_static(m, 1000, 714)

    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)