import streamlit as st
import os
from  PIL import Image

def page_intro():
    st.subheader("Welcome to")
    st.header("*Python Programming for Humanities*")
    st.write('''
    This is a prototype of an online learning platform created as an exam project for the course human-computer interaction on the Cognitive Science master's degree at Aarhus University. 

    In this prototype, we introduce one module, *Python Programming for Humanities*. 
    This module is meant to be a gentle introduction to programming for students who have not previously worked with programming. 
    ''')
    st.write('''
    We take it one step at a time, with short and interactive exercises to learn about some of the general principles of how programming can be used to work with data. 
    Examples of data in a humanities context could be surveys, social media posts, literary texts, or historical newspapers.  

    We want to help you get familiar with some programming techniques to help you produce readable and reproducible code. And to do this, we will introduce you to some of the basics of how programming can be used to communicate with computers. 
    
    Below, you see an example of code written in the programming language, Python:
    ''')
    im = Image.open(os.path.join(os.path.abspath(""),'images','python_code.png'))
    st.image(im,use_column_width=True, output_format="PNG")
    st.write("Output of code:")
    im2 = Image.open(os.path.join(os.path.abspath(""),'images','python_output.png'))
    st.image(im2,use_column_width=True, output_format="PNG")

    st.info(''' **Prerequisites**

    For this module, there are no prerequisites. All topics will be introductory, and you will try to program in this code windows within this browser without the need to install anything on your computer. 
    ''') 
    st.info('''**Learning Outcomes**

    At the end of this module, you will be able to:
    * XXX
    * XXX
    * XXX
    ''')
    
    st.markdown('''
    You can navigate the module by clicking on the topics in the left side bar, when you want to continue to the next page.  

    We hope that you will enjoy and learn some new cool stuff about programming! 

    <div style="text-align: right"> Sara Kolding and Signe Kirk Brødbæk </div>
    <div style="text-align: right"> Cognitive Science Graduate Students, Aarhus University </div>
    <div style="text-align: right"> June 10, 2022 </div>
    ''',unsafe_allow_html=True)
