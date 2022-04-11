import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide") # set to wide mode

st.header("Compare Tickets")

#PART 1) container for getting user input 
ui_col1, ui_col2, ui_col3 = st.columns([1,3,3])
with ui_col1:
    pass

with ui_col2:
    ticket_id1 = st.text_input("TICKET ID", 
                                max_chars = 20, 
                                key = "tid1",
                                help ="Please enter the ticket id. You can search it on the Data search page.")
  

with ui_col3:
    ticket_id2 = st.text_input("TICKET ID", 
                                max_chars = 20, 
                                key = "tid2",                                    
                                help ="Please enter the ticket id. You can search it on the Data search page.")



#PART 2) container for submit button and "quick look" text
col1, col2, col3 , col4, col5, col6, col7 = st.columns(7)
with col1:
    pass
with col2:
    pass
with col3:
    pass
with col4:
    pass
with col5:
    pass
with col6:
    pass
with col7:
    st.button("SUBMIT", key = "submit")


#horizontal line
st.write("Quick Look")
st.markdown("---")

# container for displaying data
r_col1, r_col2, r_col3 = st.columns([1,3,3])
with r_col1:
    st.write("Airline")
    st.write("Price")
    st.write("Arrival City")
    st.write("Departure City")
    st.write("Departure Time")
    st.write("Class")
    st.write("Duration")
    st.write("Stops")
    st.write("Flight number")

with r_col2:
    st.write("Air_India")
    st.write("$ " + "5955")
    st.write("Delhi")
    st.write("Mumbai")
    st.write("Morning")
    st.write("Economy")
    st.write("2.37")
    st.write("1")
    st.write("6E-6278")

with r_col3:
    st.write("Air_India")
    st.write("$ " + "5955")
    st.write("Delhi")
    st.write("Mumbai")
    st.write("Morning")
    st.write("Economy")
    st.write("2.37")
    st.write("1")
    st.write("6E-6278")