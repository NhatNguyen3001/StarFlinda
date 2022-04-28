import matplotlib.pyplot as plt
import csv
import streamlit as st


def draw_piechart(btn_val):
    data = get_clean_data_by_btn(btn_val)
    labels = []
    ratio = []

    for k, v in data.items():
        labels.append(k)
        ratio.append(v)


    print("label")
    for i in labels:
        print(i)

    print("ratio")
    for i in ratio:
        print(i)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    #labels = 'Vistara', 'SpiceJet', 'Indigo', 'GO FIRST', 'Air India', 'AirAsia'
    #sizes = [42.5, 1.3, 9.6, 13.5, 30.2, 2.9]

    plt.pie(ratio, labels = labels, autopct='%1.1f%%', startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    #chart.axis('equal')
    #chart.set_title(btn_val)
    
    st.pyplot(plt)



def get_clean_data_by_btn(mode):
    # DATE = 0
    AIRLINE = 1
    COUNTRY_CODE = 2
    FLIGHT_NUM_CODE = 3
    #DEPARTURE_TIME = 4
    DEPARTURE_CITY = 5
    #DURATION = 6
    STOPS = 7
    #ARRIVAL_TIME = 8
    ARRIVAL_CITY = 9
    #COST_1 = 10
    #COST_2 = 11
    CLASS = 12

    # date, 출발 시간, 도착 시간, 걸리는 시간, 가격

    data = {}
    if mode == "Date":
        data = get_basic_dict(AIRLINE)
    elif mode == "Airline":
        data = get_basic_dict(AIRLINE)
    elif mode == "Country code":
        data = get_basic_dict(COUNTRY_CODE)
    elif mode == "Flight code":
        data = get_basic_dict(FLIGHT_NUM_CODE)
    elif mode == "Departure time":
        data = get_basic_dict(AIRLINE)
    elif mode == "Departure city":
        data = get_basic_dict(DEPARTURE_CITY)
    elif mode == "Duration":
        data = get_basic_dict(AIRLINE)
    elif mode == "Stops":
        data = get_basic_dict(STOPS)
    elif mode == "Arrival time":
        data = get_basic_dict(AIRLINE)
    elif mode == "Arrival city":
        data = get_basic_dict(ARRIVAL_CITY)
    elif mode == "Cost":
        data = get_basic_dict(AIRLINE)
    elif mode == "Class":
        data = get_basic_dict(CLASS)

    return data
    

def get_basic_dict(idx):
    dic = {}
    with open("lib//data//compare_data.txt") as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # ignore header

        for key, value in dic.items():
            print(key, value)

        # make dict
        for row in dataset:
            temp_list = row.split(",")
            row_data = temp_list[idx]
            
            # check if dic has the key 
            is_key_exist = False
            for key in dic.keys():
                if key == row_data:
                    dic[key] += 1
                    is_key_exist = True
            
            if not is_key_exist:
                #key is not exist 
                #add key to dict 
                dic[row_data] = 1
        dataset.close()

    dic = get_percent_val(dic)

    return dic


def get_percent_val(dic):
    # get total value 
    total = 0

    for v in dic.values():
        total += v

    for k in dic.keys():
        num = (dic[k] / total) * 100
        dic[k] = round(num , 2) # round float

    return dic

















