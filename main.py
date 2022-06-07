'''
This is the main script of our streamlit app. 
To run this, go to the project folder and run:
- pipenv shell 
- streamlit run myfile.py
'''


# Load modules
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
import pandas as pd
#from st_aggrid import AgGrid
import io 
import os


# Import page functions 
from utils.page_introduction import page_intro
from utils.page_1_how_computers_think import page_1_how_computers_think
from utils.page_quiz import page_quiz

# set main page configurations
logo = Image.open(os.path.join(os.path.abspath(""),'images','chcaa_logo.png'))
st.set_page_config(layout="wide",page_title="Learning Platform", page_icon=logo)

# set main page configurations - padding of elements on the page
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 10rem;
                    padding-right: 13rem;
                }
        </style>
        """, unsafe_allow_html=True)

# st.markdown("""
#         <style>
#                .css-18e3th9 {
#                     padding-top: 1rem;
#                     padding-bottom: 10rem;
#                     padding-left: 5rem;
#                     padding-right: 5rem;
#                 }
#                .css-1d391kg {
#                     padding-top: 3.5rem;
#                     padding-right: 1rem;
#                     padding-bottom: 3.5rem;
#                     padding-left: 1rem;
#                 }
#                 .css-1a7jz76 h3{
#                     padding: 0rem 0px 0rem;
#                 }

#                 .css-1xv07vx hr{
#                 margin: 0.5em 0px;
#                 }

#         </style>
#         """, unsafe_allow_html=True)

# initialise app with introduction page
# if "page" not in st.session_state: 
#     st.session_state.page = "Introduction"
#     #st.session_state.page = "Introduction"

# set up sidebar
with st.sidebar:
    choose = option_menu("Scientific Programming for Humanities Students",["Introduction","---","1. How computers think", "1.1 Computer programmes", "1.2 Types and Values","1.3 Debugging","1.4 Glossary","1.5 Quiz","---","Full Glossary","Contact"],
                        icons=['house','dot','kanban','dot','dot','dot','dot','dot','dot','book','person lines fill'], #https://icons.getbootstrap.com/
                        default_index=0,
                        styles={
                            "menu-title": {"font-size": "18px"}, 
                            "container": {"background-color": "#fafafa"}, # "padding": "5!important", 
                            "icon": {"color": "black", "font-size": "18px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#0077cc"},
    }
    )

def main():
    # Setting button configurations - in first main function, followed by pages + sidebar (basic layout) - this function only sets the layout of the pages + sidebar
    ### https://www.bestcssbuttongenerator.com/#/21
    st.markdown(
            """
    <style>

    .css-1a7jz76 {
        padding: 4rem 10rem;
    }

    div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
    div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
    div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }

    #MainMenu {
        visibility: hidden;
        }
    footer {
        visibility: hidden;
        height: 0%
        }
    header {
        visibility: hidden;
        height: 0%;
        }

    div.stButton > button:first-child {
        box-shadow:inset 0px 1px 0px 0px #54a3f7;
        background:linear-gradient(to bottom, #0975b0 5%, #0061a7 100%);
        background-color:#0975b0;
        border-radius:5px;
        border:1px solid #124d77;
        display: flex;
        flex-direction: column;
        cursor:pointer;
        color:#ffffff;
        height: 3.3em;
        margin: auto;
        width: 100%;

        }
    div.stButton > button:hover {
        background:linear-gradient(to bottom, #0061a7 80%, #0a6da3 100%);
        background-color:#0061a7;
        }

    div.stButton > button:active {
        position:relative;
        top:2px;
        }

    div.stDownloadButton > button:first-child {
        background-color: #007429;
        color:#ffffff;
        border-color: #006eaf;
        height: 3.7em;
        width: 16em;
        margin: auto;
        display: block;
        }
    div.stDownloadButton > button:hover {
        background-color: #1e9047;
        color:#ffffff;
        border-color: #006eaf;
        height: 3.7em;
        width: 16em;
        }

    </style>""", unsafe_allow_html=True)

    if choose == "Introduction":
        page_quiz()
        #page_intro()
        #st.session_state = "Introduction"
    if choose == "1. How computers think":
        page_1_how_computers_think()
    if choose == "1.5 Quiz":
        page_quiz()

if __name__ == "__main__": 
	main()    

