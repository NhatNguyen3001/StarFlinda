import streamlit as st


def app():
    with st.container():
        #Website
        #PART 1) OUR MISSION
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
            Our team used Streamlit, applying Machine Learning models to process data and using Python 
            for graphic illustration.
            """, styles= {"text-align": "justify"})
        
        with mis_col2:
            st.image("https://dashboard.iammedia.am/assets/uploads/posts/thumbnails/image-1593853889761.jpg") #image for our mission

        #PART 2) ABOUT US
        abt_team_col1, abt_team_col2 = st.columns(2)

        with abt_team_col2:
            st.header("About our team")
            st.write("""Our team has begun with a small project at the RMIT Vietnam university. 
            Team members took an interest in analysing data and 
            getting predictions and suggestions based on the data by machine learning. 
            This experience motivated the founding of a start-up which is StaFiIndia.""")



        with abt_team_col1:
            st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80") #image for about our team section

        #Part 3) CHART ILLUSTRATION
        container_chart = st.container()
        with container_chart:

            chart_col1, chart_col2 = st.columns([4.6,1])

            with chart_col1:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")

            with chart_col2:
                st.image("https://scontent.fsgn13-2.fna.fbcdn.net/v/t1.15752-9/279013032_415291103297834_8777289493214965047_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=XO9DxnCSsdEAX9W9nFR&_nc_ht=scontent.fsgn13-2.fna&oh=03_AVK1_vcKQnjKoChz0eGBLU-56lr3dqdOqz82LABcEoghJA&oe=6292477F",caption = "Bar chart")
                st.image("https://scontent.fsgn8-1.fna.fbcdn.net/v/t1.15752-9/278934108_1026095314973209_571930375849437800_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=v240QdUcFUQAX8aosz1&_nc_oc=AQnnbkBWC7GzjZYFb2gfOEu8fiJ2_nlju1uoi9hzRCaMklJChd8zNGsj97GAvG0NVKY0a1BlcGr5EVo9GSYaivyZ&_nc_ht=scontent.fsgn8-1.fna&oh=03_AVIWlC02oGCjT8sIG3SFHNzkYWVXfUJ1DBm9ziEjTvhaYA&oe=62944AD8",caption = "Pie chart")

            chart_col3, chart_col4 = st.columns(2)

            with chart_col3:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Plot chart")
            
            with chart_col4:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Map")
     
                

