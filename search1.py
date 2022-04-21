import streamlit as st


def read_id(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-1]))
    my_file.close()
    return array


def read_date(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[0]))
    my_file.close()
    return array


def read_airlines(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[1]))
    my_file.close()
    return array


def read_departure(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[5]))
    my_file.close()
    return array


def read_arrival(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-4]))
    my_file.close()
    return array


def read_price(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-3]))
    my_file.close()
    return array


def read_class(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[-2]))
    my_file.close()
    return array


def read_ch_code(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[2]))
    my_file.close()
    return array


def read_num_code(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        array.append((words[3]))
    my_file.close()
    return array


def find_id_index(array, id_input):
    if id_input in array:
        index = array.index(id_input)
        return index


ticket_id = st.number_input("Input your ticker ID:", min_value=1, max_value=500, value=1, step=1)
search = st.button("Search", key="option")

if search:
    id_array = read_id("data.txt")
    ch_array = read_ch_code("data.txt")
    num_code = read_num_code("data.txt")
    date = read_date("data.txt")
    airlines = read_airlines("data.txt")
    departure = read_departure("data.txt")
    arrival = read_arrival("data.txt")
    price = read_price("data.txt")
    class_of_flight = read_class("data.txt")

    id_int = [int(x) for x in id_array]
    index = find_id_index(id_int, ticket_id)
    ch_code_final = ch_array[index]
    num_code_final = num_code[index]
    date_final = date[index]
    airlines_final = airlines[index]
    departure_final = departure[index]
    arrival_final = arrival[index]
    price_final = price[index]
    class_of_flight_final = class_of_flight[index]

    st.text("Date of flight: {}".format(date_final))
    st.text("Airlines: {}".format(airlines_final))
    st.text("ch code: {}".format(ch_code_final))
    st.text("Class: {}".format(class_of_flight_final))
    st.text("num_code: {}".format(num_code_final))
    st.text("Departed from: {}".format(departure_final))
    st.text("Arrive at: {}".format(arrival_final))
    st.text("Cost: {}".format(price_final))
