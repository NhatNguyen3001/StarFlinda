import streamlit as st


def app():

    # apply css file
    with open('lib//style//about_us_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    with st.container():
        mis_col1, mis_col2 = st.columns([1,1.5])
        with mis_col1:
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
            and make more informed decisions""", styles= {"text-align": "justify"})

            st.write("""
            Our team used Streamlit, applying Machine Learning models to process data, make a prediction and suggestion.
            Our team also uses Python for graphic illustration.
            """, styles= {"text-align": "justify"})
        
        with mis_col2:
            st.image("https://dashboard.iammedia.am/assets/uploads/posts/thumbnails/image-1593853889761.jpg") #image for our mission

        st.markdown("""
                <body>
                    <div class = "empty" style="padding: 50px;">
                    </div>
                </body>
        """, unsafe_allow_html=True)


        #PART 3) ABOUT US
        abt_team_col1, abt_team_col2 = st.columns(2)

        with abt_team_col1:
            st.image("https://images.unsplash.com/photo-1476304884326-cd2c88572c5f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80") #image for our mission
        with abt_team_col2:
            st.header("About our team")
            st.write("""Our team has begun with a small project at the RMIT Vietnam university. 
            Team members took an interest in analysing data and 
            getting predictions and suggestions based on the data by machine learning. 
            This experience motivated the founding of a start-up which is StaFiIndia.""")

            st.write("""
            StaFiIndia is the name of the company. 
            The name is a compound word for Statistic, Flight, and India. 
            This means our company will make efforts to effectively display statistics related to 
            India's domestic airline tickets with fascinating graphics.
            Our company hopes that customers will get the information they want through their services in a short period of time.
            """)


            # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)


