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
        plot, etc_items = make_pie_chart.draw_piechart(user_opt)
        
        st.pyplot(plot) # draw pie chart
        
        # show details
        if len(etc_items) >= 2:
            st.write("etc items: ")
            for item in etc_items:
                st.write(item)
    


# time 
#05:00 ~ 11:59 == "Morning"
#12:00 ~ 16:59 == "Afternoon"
#17:00 ~ 20:59 == "Evening"
#21:00 ~ 04:59 == "Night"

# to do list 
# major 
# description for each data / 

# minor 
# % value for each etc itmes 
# compare table