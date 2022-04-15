# IMPORT LIBRARY
from audioop import lin2adpcm
from operator import delitem
from os import remove
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import csv
# function 
def get_data_frame(ticket_id1, ticket_id2):
    #remove spaces 
    ticket_id1 = remove_spaces(ticket_id1)
    ticket_id2 = remove_spaces(ticket_id2)


    with open('..//lib//data//old_data.csv') as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # ignore header
        raw_tk1 = []  # raw ticket1 info on csv 
        raw_tk2 = []  # raw ticket2 info on csv  

        # search information
        for row in dataset:
            if len(raw_tk1) != 0 and len(raw_tk2) != 0:
                break  # breask after finding two tickets info

            temp_list = row.split(",")

            if int(temp_list[0]) == int(ticket_id1):
                raw_tk1 = temp_list  # get ticket1 info from cvs file
            elif int(temp_list[0]) == int(ticket_id2):
                raw_tk2 = temp_list  # get ticket2 info from cvs file

        # close file
        dataset.close()

    #set new data
    TICKET_ID = 0
    AIRLINE = 1 
    FLIGHT_ID = 2
    SOURCE_CITY = 3 
    DEPARTURE_TIME = 4
    STOPS = 5
    ARRIVAL_TIME = 6
    DESTINATION_CITY = 7
    CLASS = 8 
    DURATION = 9 
    DAYS_LEFT = 10 
    COST = 11

    new_data_dict = {raw_tk1[TICKET_ID] : [raw_tk1[AIRLINE], raw_tk1[COST], raw_tk1[SOURCE_CITY], 
                                    raw_tk1[DESTINATION_CITY], raw_tk1[DEPARTURE_TIME], raw_tk1[ARRIVAL_TIME],
                                    raw_tk1[CLASS], raw_tk1[DURATION], raw_tk1[STOPS], raw_tk1[FLIGHT_ID]],
                
                    raw_tk2[TICKET_ID] : [raw_tk2[AIRLINE], raw_tk2[COST], raw_tk2[SOURCE_CITY], 
                                        raw_tk2[DESTINATION_CITY], raw_tk2[DEPARTURE_TIME], raw_tk2[ARRIVAL_TIME],
                                        raw_tk2[CLASS], raw_tk2[DURATION], raw_tk2[STOPS], raw_tk2[FLIGHT_ID]]
    }

    return pd.DataFrame(new_data_dict)

def remove_spaces(str):
    #remove space
    str.strip()
    res = ""

    # remove spaces between chars
    for i in range(len(str)):
        if str[i] == " ":
            continue
        res += str[i]
    
    return res


def get_invalid_input(ticket_id1, ticket_id2):
    ALL_VALID = 0 
    FIRST_TK_INVALID = 1
    SECOND_TK_INVALID = 2
    BOTH_INVALID = -1 

    #remove space 
    ticket_id1 = remove_spaces(ticket_id1)
    ticket_id2 = remove_spaces(ticket_id2)

    #return invalid ticket id
    if (not ticket_id1.isnumeric()) and (not ticket_id2.isnumeric()):
        return BOTH_INVALID

    elif not ticket_id1.isnumeric():
        return FIRST_TK_INVALID

    elif not ticket_id2.isnumeric():
        return SECOND_TK_INVALID

    return ALL_VALID

def app():
    # SETTING

    # apply css file
    with open('../lib/style/compare_tickets_app.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)


    # default table data
    def_data = {'The first ticket ID' : ['SpiceJet', '5953', 'Delhi', 'Mumbai', 'Evening', 'Night', 'Economy', '2.17', 'zero', 'SG-8709'],
            'The second ticket ID' : ['SpiceJet', '5953', 'Delhi', 'Mumbai', 'Early_Morning', 'Morning', 'Economy', '2.33', 'zero', 'SG-8157']
    }

    def_idx = ['Airline', 'cost', 'source city', 'destination city', 'departure time', 
                        'arrival time', 'class', 'duration', 'stops', 'flight ID']

    # set table
    compare_df = pd.DataFrame(def_data)
    compare_df.index = def_idx # set index
    compare_df.style.set_properties(subset=[' '], **{'width': '100px'})
  
  
    # BUILDING A WEBSITE
    st.header("Compare Tickets") # write a title

    #PART 1) Get user input 
    ui_col1, ui_col2, ui_col3 = st.columns([1,3,3])

    with st.form("compare_form"):

        with ui_col1:
            pass

        with ui_col2:
            ticket_id1 = st.text_input("TICKET ID", 
                                        value = 0,
                                        max_chars = 20, 
                                        key = "tid1",
                                        help ="Please enter the ticket id. You can search it on the Data search page.")
        

        with ui_col3:
            ticket_id2 = st.text_input("TICKET ID", 
                                        value = 1,
                                        max_chars = 20, 
                                        key = "tid2",                                    
                                        help ="Please enter the ticket id. You can search it on the Data search page.")
    #PART 2) submit form
        sm_col1, sm_col2, sm_col3 = st.columns([3,3,1])
        invalid_input = 0
        with sm_col1:
            pass
        with sm_col2:
            pass
        with sm_col3:
            submit_button = st.form_submit_button(label="Submit")
            if submit_button: #function when submit button is turned on
                #check data input 
                invalid_input = get_invalid_input(ticket_id1, ticket_id2) # return 0, if all inputs are valid

                if (not invalid_input) :
                    # get new data frame 
                    new_data_frame = get_data_frame(ticket_id1, ticket_id2)

                    #update data frame
                    compare_df = new_data_frame #update data
                    compare_df.index = def_idx # set index
                    compare_df.style.set_properties(subset=[' '], **{'width': '100px'}) # set style
                
        if invalid_input: 
            FIRST_TK_INVALID = 1
            SECOND_TK_INVALID = 2
            BOTH_INVALID = -1 
            msg_invalid_tk = ""

            # set error message 
            if (invalid_input == BOTH_INVALID) :
                msg_invalid_tk += "Both"
            elif (invalid_input == FIRST_TK_INVALID):
                msg_invalid_tk += "The first"
            elif (invalid_input == SECOND_TK_INVALID):
                msg_invalid_tk += "The second"

            st.error(msg_invalid_tk + " ticket ID is invalid. Please check again.")


    #Quick look and horizontal line
    st.write("Quick Look")
    st.markdown("---")

    #PART 3) displaying data
    st.table(compare_df)
