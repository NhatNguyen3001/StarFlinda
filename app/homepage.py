import streamlit as st


def app():

    # apply css file
    with open('lib//style//homepage.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    with st.container():
        #Website
        #Part 0) Introduction 
        with st.container():
            st.title("Welcome to StaFiIndia")
            st.image("lib/img/welcome.jpg"  )
            st.write("""
            Hello, welcome to StaFiIndia. Our company focuses on data visualization of the India local flight ticket information. 
            The company provides data in various ways such as graphs, tables and charts and the user is allowed to take granular control 
            to acquire specific data that the user desired. 
            You can also search the data and compare two data. Feel free to enjoy our services and contact us if you need any help.
            """)
        


        #Part 1) SERVICES ILLUSTRATION
        container_chart = st.container()
        with container_chart:
            st.title("Beautiful data visualization")
            st.image("lib/img/statics.jpg", width=500, caption = "Various charts and graphs")
            st.write("description")


        #Part 1-1) EXPLAIN EACH CHART
        with st.container():
            st.title("Charts detail")
            

            # TABLE
            chart1_col1, chart1_col2 = st.columns(2)

            st.title("1. Table")
            with chart1_col1:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6" , caption = "Table")


            with chart1_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                



            # BAR CHART
            chart2_col1, chart2_col2 = st.columns(2)

            st.title("2. Bar chart")
            with chart2_col1:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                
                

            with chart2_col2:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")


            # PIE CHART
            chart3_col1, chart3_col2 = st.columns(2)

            st.title("3. Pie chart")
            with chart3_col1:
                st.image("https://scontent.fsgn13-2.fna.fbcdn.net/v/t1.15752-9/279013032_415291103297834_8777289493214965047_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=XO9DxnCSsdEAX9W9nFR&_nc_ht=scontent.fsgn13-2.fna&oh=03_AVK1_vcKQnjKoChz0eGBLU-56lr3dqdOqz82LABcEoghJA&oe=6292477F",caption = "Bar chart")

            with chart3_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                
            # PLOT CHART
            chart4_col1, chart4_col2 = st.columns(2)

            st.title("4. Plot chart")
            with chart4_col1:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                

            with chart4_col2:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")
                

            # MAP
            chart5_col1, chart5_col2 = st.columns(2)

            st.title("5. Map")
            with chart5_col1:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")

            with chart5_col2:
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                
                
        #Part 1-2) EXPLAIN DATA SEARCH PAGE

            st.title("DATA SEARCH")
            with st.container():
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")

            with st.container():
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})



        #Part 1-3) EXPLAIN DATA COMPARE PAGE

            st.title("DATA COMPARISION")
            with st.container():
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")

            with st.container():
                st.header("What data does staFiIdia show?")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.header("What are things that you can control?")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.header("Guide")
                st.write("""
                        Step 1) Please choose one of the data types on the select box.\n
                        Step 2) Check out a beautiful pie chart StaFiIndia provide.\n
                        Step 3) More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})






        #PART 2) OUR MISSION
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


