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

from streamlit_ace import st_ace
import sys
import os
from io import StringIO
import contextlib

# set up root directory
root_dir = os.path.abspath("")

# load logos 
logo = Image.open(os.path.join(root_dir,'images','chcaa_logo.png'))
# Setting main page configurations
st.set_page_config(layout="wide",page_title="Learning Platform", page_icon="😊")

# Setting main page configurations - padding of elements on the page

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
                .css-1a7jz76 h3{
                    padding: 0rem 0px 0rem;
                }

                .css-1xv07vx hr{
                margin: 0.5em 0px;
                }

        </style>
        """, unsafe_allow_html=True)

if "page" not in st.session_state: 
    st.session_state.page = "Welcome"


def page_main():
    st.write("Page1")

def page2():
    st.write("Page2")

def main():
    # Setting button configurations - in first main function, followed by pages + sidebar (basic layout) - this function only sets the layout of the pages + sidebar
    ### https://www.bestcssbuttongenerator.com/#/21
    st.markdown(
            """
    <style>

    .css-1a7jz76 {
        padding: 4rem 1rem;
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

    pages = {
        "Welcome": page_main, # title of button is "Welcome"
        "Standardisation": page2
    }


    col1, col2 = st.sidebar.columns([1,1])

    if st.sidebar.button("Standardisation"):
        st.session_state.page = "Standardisation"
    if st.sidebar.button("Welcome"):
        st.session_state.page = "page_main"

    pages[st.session_state.page]()

if __name__ == "__main__": 
	main()    

