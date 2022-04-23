import streamlit as st
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Vistara', 'SpiceJet', 'Indigo', 'GO FIRST', 'Air India', 'AirAsia'
sizes = [42.5, 1.3, 9.6, 13.5, 30.2, 2.9]


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title('Economy Class')


labels2 = 'Vistara', 'Air India'
sizes2 = [54.2, 45.8]

fig2, ax2 = plt.subplots()
ax2.pie(sizes2, labels = labels2, autopct = '%1.1f%%', startangle = 90)
ax2.axis('equal')
ax2.set_title('Business Class')


st.pyplot(fig1)
st.pyplot(fig2)