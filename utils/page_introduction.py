import streamlit as st
import os
from  PIL import Image

def page_intro():
    logo = Image.open(os.path.join(os.path.abspath(""),'images','chcaa_logowithtext.png'))
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

    We hope that you will enjoy and learn some new cool stuff about programming! 

    Sara Kolding and Signe Kirk Brødbæk
    
    Cognitive Science Graduate Students, Aarhus University 
    
    June 10, 2022
    ''')
