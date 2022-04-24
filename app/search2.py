import streamlit as st

chosen_ch_code = []
chosen_num_code = []
chosen_departure = []
chosen_arrival = []
chosen_date = []
chosen_airlines = []
chosen_class = []
chosen_price = []


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


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def find_index(array1, array2, number_input):
    if number_input in array2:
        chosen_index = array2.index(number_input)
    else:
        array2.append(number_input)
        array2.sort()
        index = array2.index(number_input)
        if index == 0:
            chosen_index = 1
        elif index == (len(array2) - 1):
            chosen_index = index - 1
        else:
            result_1 = abs(number_input - array2[index - 1])
            result_2 = abs(array2[index + 1] - number_input)
            if result_1 < result_2:
                chosen_index = index - 1
            elif result_1 > result_2:
                chosen_index = index + 1
            else:
                chosen_index = index - 1
    chosen_value = array2[chosen_index]
    final_index = array1.index(chosen_value)
    return final_index


def app():
    ch_array = read_ch_code("lib//data//data.txt")
    num_code = read_num_code("lib//data//data.txt")
    date = read_date("lib//data//data.txt")
    airlines = read_airlines("lib//data//data.txt")
    departure = read_departure("lib//data//data.txt")
    arrival = read_arrival("lib//data//data.txt")
    price = read_price("lib//data//data.txt")
    class_of_flight = read_class("lib//data//data.txt")

    departure_input = st.selectbox("Select your departure", ("Bangalore", "Delhi",
                                                            "Kolkata", "Chennai",
                                                            "Hyderabad", "Mumbai"))
    arrival_input = st.selectbox("Select your arrival", ("Mumbai", "Delhi", "Chennai"))
    class_input = st.selectbox("Select your class", ("economy", "business"))
    price_input = st.slider("Choose the approximately price", min_value=2000, max_value=94000, value=2000, step=1)
    search = st.button("Search", key="option")

    index_keep_final = "" #init

    if search:
        index_keep_1 = [i for i, x in enumerate(departure) if x == departure_input]
        index_keep_2 = [i for i, x in enumerate(arrival) if x == arrival_input]
        index_keep_3 = [i for i, x in enumerate(class_of_flight) if x == class_input]
        index_keep_4 = intersection(index_keep_1, index_keep_2)
        index_keep_final = intersection(index_keep_4, index_keep_3)
    if len(index_keep_final) == 0:
        st.write("Sorry, there is no result for your search, please try again")
    else:
        for i in index_keep_final:
            chosen_ch_code.append(ch_array[i])
            chosen_num_code.append(num_code[i])
            chosen_departure.append(departure[i])
            chosen_arrival.append(arrival[i])
            chosen_date.append(date[i])
            chosen_airlines.append(airlines[i])
            chosen_class.append(class_of_flight[i])
            chosen_price.append(price[i])

        price_int_1 = [int(x) for x in chosen_price]
        price_int_2 = [int(x) for x in chosen_price]
        find_data = find_index(price_int_1, price_int_2, price_input)
        final_ch_code = chosen_ch_code[find_data]
        final_num_code = chosen_num_code[find_data]
        final_departure = chosen_departure[find_data]
        final_arrival = chosen_arrival[find_data]
        final_date = chosen_date[find_data]
        final_airlines = chosen_airlines[find_data]
        final_class = chosen_class[find_data]
        final_price = chosen_price[find_data]

        st.text("Date of flight: {}".format(final_date))
        st.text("Airlines: {}".format(final_airlines))
        st.text("ch code: {}".format(final_ch_code))
        st.text("num_code: {}".format(final_num_code))
        st.text("Class: {}".format(final_class))
        st.text("Departed from: {}".format(final_departure))
        st.text("Arrive at: {}".format(final_arrival))
        st.text("Cost: {}".format(final_price))