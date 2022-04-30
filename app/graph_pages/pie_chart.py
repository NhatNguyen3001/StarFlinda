import streamlit as st
import matplotlib.pyplot as plot
from prog import make_pie_chart


def app():

    st.title("Pie chart")
    with st.container():
        st.write("description of pie chart")

    with st.container():
        user_opt = st.selectbox("Pie chart about:",
                            ('Date', 'Airline', 'Country code', 'Departure time', 'Departure city', 
                            'Duration','Stops', 'Arrival time', 'Arrival city', 'Cost', 'Class')
        )

    with st.container():
        plot, etc_dict = make_pie_chart.draw_piechart(user_opt)
        
        st.pyplot(plot) # draw pie chart
        
        # show etc details
        etc_items_len = len(etc_dict)
        if etc_items_len >= 2:
            items_list_str = ""
            last_item_idx = etc_items_len - 1
            idx = 0
            
            print(etc_items_len)
            for k in etc_dict.keys():
                items_list_str += k + "(" + str(etc_dict[k]) + "%)"
                if (idx != last_item_idx):
                    items_list_str += ",   "

                idx = idx + 1
            


            #display detail descrption
            st.write("Some elements accounting for less than 5% of the total were found. The elements were "
                        + items_list_str + ". These elements were consolidated in the 'etc' field on the chart.")
        
        # show detail description
        if user_opt == 'Departure time' or user_opt == 'Arrival time':
            st.write("The time range follows the criterion below.")
            st.write("""
                        From 05:00 to 11:59: Morning \n
                        From 12:00 to 16:59: Afternoon \n
                        From 17:00 to 20:59: Evening \n
                        From 21:00 to 04:59: Night \n
                    """)
