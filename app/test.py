import pandas as pd

# def_data = {'The first ticket ID': ['Vistara', '4792', '24/03/22' 'Bangalore', 'Mumbai', '19:55',
#                                             '14:30', 'Economy', '18h 35m', '1-stop', 'UK-893'],

#                     'The second ticket ID': ['Vistara', '4792', '24/03/22', 'Bangalore', 'Mumbai', '7:55',
#                                              '10:00', 'Economy', '26h 05m', '1-stop', 'UK-897']
#                     }

# def_idx = ['Airline', 'Cost', 'Date', 'Departure City', 'Arrival City', 'Departure Time',
#             'Arrival Time', 'Class', 'Duration', 'Layover/Stopover', 'Flight ID']

def_data = {'The first ticket ID' : ['SpiceJet', '5953', 'Delhi', 'Mumbai', 'Evening', 'Night', 'Economy', '2.17', 'zero', 'SG-8709'],
        'The second ticket ID' : ['SpiceJet', '5953', 'Delhi', 'Mumbai', 'Early_Morning', 'Morning', 'Economy', '2.33', 'zero', 'SG-8157']
}

def_idx = ['Airline', 'cost', 'source city', 'destination city', 'departure time', 
                    'arrival time', 'class', 'duration', 'stops', 'flight ID']

# set table
compare_df = pd.DataFrame(def_data)
compare_df.index = def_idx  # set index

compare_df.style