import streamlit as st
import pandas as pd
import altair as alt
from prog import check_user_input


def app():
    # Hide menu
    hide_menu = """
    <style>
    #MainMenu { visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)

    st.title("CHARTS")

    # Link css footer
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    # Sidebar
    # Button css
    buttoncss = st.markdown("""
    <style>
    div.stButton > button:first-child {
        width:700px;
        height:50px;
        justify-content: left;
        font-family: "IBM Plex Sans", sans-serif;
        font-size: 0.8rem;
    }
    </style>""", unsafe_allow_html=True)

    # Function
    # CSV file
    csv_url = 'https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data.csv'
    df = pd.read_csv(csv_url)

    st.text("Please input following format: mm/dd/yyyy")
    d = st.text_input('Choose the date')
    day = st.write(d)


    ###Price_bar
    pricechart = alt.Chart(df).mark_bar().encode(
        y=alt.Y('count(airline):O', title="Number of flight"),
        x=alt.X('class:N', title="Class"),
        color='class:N',
        column='airline:N'
    ).transform_filter(alt.FieldEqualPredicate(field='date', equal=d)
                    ).properties(height=500, width=60)

    ##Price button
    is_valid_input = check_user_input.valid_ui_bar(d)
    if d == "":
        # show default chart
        st.write(pricechart_default)

        # explain charts

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    if d:
        st.altair_chart(pricechart)

        # Footer
        st.markdown("""
        <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
        <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
        </nav>
        """, unsafe_allow_html=True)
=======
=======
>>>>>>> Stashed changes
    elif 0 > is_valid_input:
        #invalid user input is dectected

        #error message 
        INVALID_FORMAT = -1 

        err_msg = "The format is invalid." if is_valid_input == INVALID_FORMAT else "The date is out of scope."

        # show error message if user input is not valid
        st.error(err_msg + " Please check provided guidance and try again.")

        # show default chart
        st.write(pricechart_default)

        # explain charts

    elif d and is_valid_input:
        # show chart if user input is valid
        st.write(pricechart)

        # explain charts

 
    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)
>>>>>>> Stashed changes
