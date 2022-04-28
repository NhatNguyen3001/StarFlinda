import matplotlib.pyplot as plt
import csv

from numpy import row_stack


def get_piechart():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Vistara', 'SpiceJet', 'Indigo', 'GO FIRST', 'Air India', 'AirAsia'
    sizes = [42.5, 1.3, 9.6, 13.5, 30.2, 2.9]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    ax1.set_title('Economy Class')

    return fig1


def get_data(mode):
    DATE = 0
    AIRLINE = 1
    COUNTRY_CODE = 2
    FLIGHT_NUM_CODE = 3
    DEPARTURE_TIME = 4
    DEPARTURE_CITY = 5
    DURATION = 6
    STOPS = 7
    ARRIVAL_TIME = 8
    ARRIVAL_CITY = 9
    COST_1 = 10
    COST_2 = 11
    CLASS = 12


def get_date_data(idx):
    with open("lib//data//compare_data.txt") as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)  # ignore header


        # make dict
        for row in dataset:
            temp_list = row.split(" ")
            row_data = temp_list[idx]
            print(row_data + " ")

        dataset.close()


get_date_data(0)














