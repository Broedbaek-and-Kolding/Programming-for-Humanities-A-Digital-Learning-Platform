"""
In terminal:
- cd ..
- source hci_env/bin/activate
- cd _hci_exam/
- streamlit run ace_editor_demo.py 

to stop: control + c
"""

from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 

import streamlit as st
from streamlit_ace import st_ace
import sys
import os
from io import StringIO
import contextlib

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

root_dir = os.path.abspath("")

logo = Image.open(os.path.join(root_dir,'images','chcaa_logowithtext.png'))
#profile = Image.open(r'C:\Users\13525\Desktop\medium_profile.png')
if choose == "Introduction":
    st.image(logo, width=500 )
    st.write('''
    Welcome! 

    This is a prototype of an online learning platform created as an exam project for the course human-computer interaction as a part of our study. 

    In this prototype, we include one module, *Scientific programming for humanities students*. 
    This module is meant to be a gentle introduction to programming and *text analysis* for students who have not worked with computers in this way before. 

    We take it one step at a time, with short and interactive introductions to learn about some of the general principles in which computers can be used to study text data. Examples of text data could be social media posts, literary texts, or historical newspapers.  

    We want to help you get familiar with some programming techniques to help you produce readable and reproducible code. And to do this, we will also introduce you to some basics on how computers work. 

    For this module, there are no prerequisites. All topics will be introductory, and you will be able to try programming in this browser without the need to install anything on your computer. 
    ''') 
    st.info('''
    At the end of this module, you will be able to:
    * XXX
    * XXX
    * XXX
    ''')
    
    st.write('''
    You can navigate the module by clicking on the topics in the left side bar, when you want to continue to the next page.  

    We hope that you will enjoy and learn some new cool stuff about programming! \n\n\n

    Sara Kolding and Signe Kirk Brødbæk \n
    Cognitive Science Graduate Students, Aarhus University \n
    June 10, 2022
    ''')

if choose == "1. How computers think":
# Spawn a new Ace editor
    content = st_ace(placeholder='Write code here',language='python')

    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    code = content

    st.write("Output of code:")
    with stdoutIO() as s:
        try:
            exec(code)
        except:
            st.warning("Something is wrong with the code.")
            exec(code)
            

        st.text(str(s.getvalue()))

