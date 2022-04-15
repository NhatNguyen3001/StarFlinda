import streamlit as st
# REF : https://github.com/dataprofessor/multi-page-app/blob/main/multiapp.py
class Multi_app:
    def __init__(self):
        self.apps_list = []

    def add_app(self, app_title, func_name):
        self.apps_list.append({
            "Application title": app_title,
            "function": func_name
        })

    def run(self):
        app = st.selectbox(
            'Navigation',
            self.apps_list,
            format_func=lambda app: app['Application title'])

        app['function']()