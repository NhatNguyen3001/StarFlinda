import streamlit as st


def app():
    with st.container():
        #Website
        #PART 1) OUR MISSION
        mis_col1, mis_col2 = st.columns(2)
        with mis_col1:
            st.image("https://images.unsplash.com/photo-1476304884326-cd2c88572c5f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80") #image for our mission

        with mis_col2:
            st.header("Background")
            st.write("""
            EasyJet CEO John Lundgren had a data science team 
            to create an algorithm that predicted insight on food items, 
            Southwest Airlines developed a model to forecast monthly fuel consumption. 
            These examples have proven the demanding need in researching flights. """)

            st.write("""
            Our objective is to assist flying consumers in checking airline information 
            in luxury service, premium class flights and low-cost travel. 
            Ticket price, flight direction, and frequency, which can be displayed 
            in pre-sorted tables and graphs on a website. 
            As a result, users can obtain a summary view of flight information 
            and make more informed decisions""")

            st.write("""
            Our team used Streamlit, applying Machine Learning models to process data and using Python 
            for graphic illustration.
            """)

        #PART 2) ABOUT US
        abt_team_col1, abt_team_col2 = st.columns(2)

        with abt_team_col1:
            st.header("ABOUT OUR TEAM")
            st.write("""Our team has begun with a small project at the RMIT Vietnam university. 
            Team members took an interest in analysing data and 
            getting predictions and suggestions based on the data by machine learning. 
            This experience motivated the founding of a start-up which is StaFiIndia.""")



        with abt_team_col2:
            st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80") #image for about our team section