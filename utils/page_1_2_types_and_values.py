import streamlit as st
import os
from  PIL import Image

def page_1_2_types_and_values():
    st.title("1.2 Types and Values")
    st.write('''
    This page is under construction and, thus, for now, there is no content on this page. 

    You can continue to learn about programming in Python on the next pages.
    
    Sorry for the inconvenience! 
    ''')
    
    im = Image.open(os.path.join(os.path.abspath(""),'images','page_under_construction.png'))
    st.image(im,use_column_width=True, output_format="PNG")