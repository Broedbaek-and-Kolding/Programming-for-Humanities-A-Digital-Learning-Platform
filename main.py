'''
This is the main script of our streamlit app. 
To run this, go to the project folder and run:
- pipenv shell 
- streamlit run myfile.py
'''

# Load modules
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from  PIL import Image
#import numpy as np
#import cv2
#import pandas as pd
#from st_aggrid import AgGrid
#import io 
import os

# Import page functions 
from utils.page_introduction import page_intro
from utils.page_why_programming import page_why_programming
from utils.page_1_how_computers_think import page_1_how_computers_think
from utils.page_1_1_computer_programmes import page_1_1_computer_programmes
from utils.page_1_2_types_and_values import page_1_2_types_and_values
from utils.page_glossary import page_glossary
from utils.page_quiz import page_quiz
from utils.page_contact import page_contact
from utils.page_survey import page_survey


# set main page configurations
#logo = Image.open(os.path.join(os.path.abspath(""),'images','chcaa_logo.png'))
st.set_page_config(layout="wide",page_title="Learning Platform", page_icon="🐍")

# set main page configurations - padding of elements on the page
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 7rem;
                    padding-right: 13rem;
                }

               .css-1m3vq7  {
                    padding-top: 4.5rem;
                    padding-bottom: 1.5rem;
                    padding-left: 1.2rem;
                    padding-right: 1.2rem;
                    width: 23rem;
                }

        </style>
        """, unsafe_allow_html=True)


# set up sidebar
with st.sidebar:
    im = Image.open(os.path.join(os.path.abspath(""),'images','chcaa_logowithtext.png'))
    st.image(im,use_column_width=True, output_format="PNG")

    # page state
    if "page" not in st.session_state:
        st.session_state.page = 1

    # prepare badges from quiz
    if 'counter' not in st.session_state:
        st.session_state.counter = False

    if 1 <= st.session_state.counter <= 6 and st.session_state.badge == "q1":
        badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_bronze.png'))
        st.image(badge1, width=40)
    elif 6 < st.session_state.counter <= 8 and st.session_state.badge == "q1":
        badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_silver.png'))
        st.image(badge1, width=40)
    elif st.session_state.counter > 8 and st.session_state.badge == "q1":
        badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_gold.png'))
        st.image(badge1, width=40)
    
    choose = option_menu("Scientific Programming for Humanities Students",
                            ["Introduction","---","0. Why Programming?","---","1. How Computers Think", "1.1 Computer Programmes", 
                            "1.2 Types and Values","1.3 Quiz","1.4 Glossary","---","1.5 Survey","---","Contact"],
                        icons=['house','dot','people','dot','display','dot','dot','stopwatch','book','dot','ui-radios','dot','envelope','person lines fill'], #https://icons.getbootstrap.com/
                        default_index=0,
                        styles={
                            "menu-title": {"font-size": "18px"}, 
                            "container": {"background-color": "#fafafa"}, #"padding": "5!important", 
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
        background:linear-gradient(to bottom, #0077cc 5%, #1e62d0 100%);
        background-color:#0077cc;
        border-radius:6px;
        display:inline-block;
        cursor:pointer;
        color:#ffffff;
        font-size:16px;
        display: flex;
        flex-direction: column;
        cursor:pointer;
        color:#ffffff;
        height: 3.3em;
        margin: auto;
        width: 100%;

        }
    div.stButton > button:hover {
        background:linear-gradient(to bottom, #0077cc 80%, #0a6da3 100%);
        background-color:#0077cc;
        }

    div.stButton > button:active {
        position:relative;
        top:2px;
        }

    .streamlit-expanderHeader {
    font-size: 16px;
    }

    .css-1c20onu {
    font-size: 18px;
    }

    </style>""", unsafe_allow_html=True)

    # If pressed on each tab, what should be shown
    if choose == "Introduction":
        page_intro()
        st.session_state.page += 1
    if choose == "0. Why Programming?":
        page_why_programming()
        st.session_state.page += 1
    if choose == "1. How Computers Think":
        page_1_how_computers_think()
        st.session_state.page += 1
    if choose == "1.1 Computer Programmes":
        page_1_1_computer_programmes()
        st.session_state.page += 1
    if choose == "1.2 Types and Values":
        page_1_2_types_and_values()
        st.session_state.page += 1
    if choose == "1.3 Quiz":
        page_quiz()
        st.session_state.page += 1
        #print(st.session_state.counter, st.session_state.badge)
    if choose == "1.4 Glossary":
        page_glossary()
        st.session_state.page += 1
    if choose == "1.5 Survey":
        page_survey()
        st.session_state.page += 1
    if choose == "Contact": 
        page_contact()
        st.session_state.page += 1


components.html(
    f"""
        <p>{st.session_state.page}</p>
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
    """,
    height=0
)


if __name__ == "__main__": 
	main()    

