import streamlit as st
from multi_app import Multi_app
from apps import about_us, compare_tickets, contact_us


my_app = Multi_app()

# set navigation bar 
my_app.add_app("Home", about_us.app)
my_app.add_app("Data Search", about_us.app)
my_app.add_app("Compare Tickets", compare_tickets.app)
my_app.add_app("About Us", about_us.app)
my_app.add_app("Contact Us", contact_us.app)

# run my app
my_app.run()
