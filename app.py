import streamlit as st
import pickle
import pandas as pd
model = pickle.load(open('model.sav', 'rb'))

st.title('Prediction')
st.sidebar.header('Data')


class_to_view = st.slider("Choose class (Economy: 1, Business: 0):", 0, 1, 0, 1, key=1)
source_city = st.slider('Source city (Bangalore: 0, Chennai: 1, Delhi: 2, Hyderabad: 3, Kokalta: 4, Mumbai: 5):', 0, 5, 0, key=2)
arrival_city = st.slider('Arrival (Bangalore: 0, Chennai: 1, Delhi: 2, Hyderabad: 3, Kokalta: 4, Mumbai: 5):', 0, 5, 0, key=3)
airline = st.slider('Airline (AirAsia: 0, Air_India: 1, GO_FIRST: 2, INDIGO: 3, SpiceJet: 4, Vistara: 5):', 0, 5, 0, key=5)
stops = st.slider("Stops", 0, 2, 0, key=7)
days_left_to_flight = st.slider("Days left to flight:", 1, 49, 1, key=6)

report_data = pd.DataFrame({"airline": [airline], "source_city": [source_city], "stops": [stops],
                            "arrival_city": [arrival_city], "class": [class_to_view],
                            "days_left_to_flight": [days_left_to_flight]})


price_predict = model.predict(report_data)
st.write("The approximately price for the flight is:", price_predict)

