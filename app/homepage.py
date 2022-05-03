import streamlit as st



def app():
    with st.container():
        #Website
        #Part 0) Introduction 
        with st.container():
            st.title("Welcome to StaFiIndia")
            st.write("description")

        #Part 1) SERVICES ILLUSTRATION
        container_chart = st.container()
        with container_chart:
            st.title("Beautiful data visualization")
            st.write("description")
            chart_col1, chart_col2 = st.columns([4.6,1])

            with chart_col1:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6",caption = "Table")

            with chart_col2:
                st.image("https://scontent.fsgn13-2.fna.fbcdn.net/v/t1.15752-9/279013032_415291103297834_8777289493214965047_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=XO9DxnCSsdEAX9W9nFR&_nc_ht=scontent.fsgn13-2.fna&oh=03_AVK1_vcKQnjKoChz0eGBLU-56lr3dqdOqz82LABcEoghJA&oe=6292477F",caption = "Bar chart")
                st.image("https://scontent.fsgn8-1.fna.fbcdn.net/v/t1.15752-9/278934108_1026095314973209_571930375849437800_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=v240QdUcFUQAX8aosz1&_nc_oc=AQnnbkBWC7GzjZYFb2gfOEu8fiJ2_nlju1uoi9hzRCaMklJChd8zNGsj97GAvG0NVKY0a1BlcGr5EVo9GSYaivyZ&_nc_ht=scontent.fsgn8-1.fna&oh=03_AVIWlC02oGCjT8sIG3SFHNzkYWVXfUJ1DBm9ziEjTvhaYA&oe=62944AD8",caption = "Pie chart")

            chart_col3, chart_col4 = st.columns([1,1])

            with chart_col3:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970884752187994122/plot.PNG", width = 410, caption = "Plot chart")
            
            with chart_col4:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970885256729231380/unknown.png", width = 520, caption = "Map")
     
        #Part 1-1) EXPLAIN EACH CHART
        with st.container():
            st.title("Charts detail")
            

            # TABLE
            chart1_col1, chart1_col2 = st.columns(2)

            with chart1_col1:
                st.image("https://scontent.fsgn13-1.fna.fbcdn.net/v/t1.15752-9/279376534_566833528012167_1745783498800769969_n.png?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_ohc=doGDvopum8gAX8_seOU&_nc_ht=scontent.fsgn13-1.fna&oh=03_AVIP60MQ8WFFxJO1Uylrf1ZiueQEmTmlVNtfD5tFy8lUwQ&oe=6292E5E6", width = 500, caption = "Table")


            with chart1_col2:
                st.header("1. Table")
                st.write("**---------------------------------WHAT DOES TABLE SHOW?------------------------------**")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**---------------------------------------------GUIDE-------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                



            # PIE CHART
            chart2_col1, chart2_col2 = st.columns(2)

            with chart2_col1:
                st.header("2. Pie chart")
                st.write("**-------------------------------WHAT DOES PIE CHART SHOW?---------------------------**")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**---------------------------------------------GUIDE-------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                
                

            with chart2_col2:
                st.image("https://scontent.fsgn8-1.fna.fbcdn.net/v/t1.15752-9/278934108_1026095314973209_571930375849437800_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=v240QdUcFUQAX8aosz1&_nc_oc=AQnnbkBWC7GzjZYFb2gfOEu8fiJ2_nlju1uoi9hzRCaMklJChd8zNGsj97GAvG0NVKY0a1BlcGr5EVo9GSYaivyZ&_nc_ht=scontent.fsgn8-1.fna&oh=03_AVIWlC02oGCjT8sIG3SFHNzkYWVXfUJ1DBm9ziEjTvhaYA&oe=62944AD8",caption = "Pie chart")


            # BAR CHART
            chart3_col1, chart3_col2 = st.columns(2)

            with chart3_col1:
                st.image("https://scontent.fsgn13-2.fna.fbcdn.net/v/t1.15752-9/279013032_415291103297834_8777289493214965047_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_ohc=XO9DxnCSsdEAX9W9nFR&_nc_ht=scontent.fsgn13-2.fna&oh=03_AVK1_vcKQnjKoChz0eGBLU-56lr3dqdOqz82LABcEoghJA&oe=6292477F",width=450,caption = "Bar chart")

            with chart3_col2:
                st.header("3. Bar chart")
                st.write("**-----------------------------WHAT DOES BAR CHART SHOW?---------------------------**")
                st.write("The bar chart is going to illustrate the number of flight which is grouped by class of each arline agency.", 
                        styles= {"text-align": "justify"})
                
                st.write("**------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------**")
                st.write("""You can enter the date in which you want to the the number of flight. 
                            After you enter, the bar chart will alter base on your user input. If nothing is entered, the default bar chart is showed""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**---------------------------------------------GUIDE-------------------------------------------**")
                st.write("""
                        **Step 1)** Please enter the date you want to see the number of flight.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        """, styles= {"text-align": "justify"})
                                
            # PLOT CHART
            chart4_col1, chart4_col2 = st.columns(2)

            with chart4_col1:
                st.header("4. Plot chart")
                st.write("**-----------------------------WHAT DOES PLOT CHART SHOW?--------------------------**")
                st.write("StaFlindia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**---------------------------------------------GUIDE-------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})

            with chart4_col2:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970884752187994122/plot.PNG", width = 410, caption = "Plot chart")
                

            # MAP
            chart5_col1, chart5_col2 = st.columns(2)

            with chart5_col1:
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970885256729231380/unknown.png", width = 520, caption = "Map")

            with chart5_col2:
                st.header("5. Map")
                st.write("**-----------------------------WHAT DOES MAP CHART SHOW?---------------------------**")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**---------------------------------------------GUIDE-------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})
                                
                
        #Part 1-2) EXPLAIN DATA SEARCH PAGE

            st.title("DATA SEARCH")
            with st.container():
                st.image("https://media.discordapp.net/attachments/872860802107990116/970959338598432778/unknown.png?width=1171&height=670", caption = "Data Search")

            with st.container():
                st.write("**---------------------------------------------------------------------------------WHAT DOES DATA SEARCH DO?------------------------------------------------------------------------------**")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**-----------------------------------------------------------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------------------------------------------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**------------------------------------------------------------------------------------------------GUIDE--------------------------------------------------------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
                        """, styles= {"text-align": "justify"})



        #Part 1-3) EXPLAIN DATA COMPARE PAGE

            st.title("DATA COMPARISION")
            with st.container():
                st.image("https://cdn.discordapp.com/attachments/872860802107990116/970948034500362250/unknown.png",caption = "Data Comparison")

            with st.container():
                st.write("**---------------------------------------------------------------------------------WHAT DOES DATA SEARCH DO?------------------------------------------------------------------------------**")
                st.write("StaFiIndia provides more than ten pie charts by each data type so that you can acquire the data you want.", 
                        styles= {"text-align": "justify"})
                
                st.write("**-----------------------------------------------------------------------------WHAT ARE THINGS YOU CAN CONTROL?----------------------------------------------------------------------**")
                st.write("""You can select one data type. 
                            Provided data types are 'Date', 'Airline', 'Country code', 'Departure time', 
                            'Departure city', 'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost' and 'Class'.""" , 
                            styles= {"text-align": "justify"})
                
                st.write("**------------------------------------------------------------------------------------------------GUIDE--------------------------------------------------------------------------------------------**")
                st.write("""
                        **Step 1)** Please choose one of the data types on the select box.\n
                        **Step 2)** Check out a beautiful pie chart StaFiIndia provide.\n
                        **Step 3)** More details will be provided when selecting some data types, for example, departure time and arrival time.\n
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


