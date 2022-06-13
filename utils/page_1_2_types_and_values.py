import streamlit as st
import os
from  PIL import Image
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO

from utils.ace_editor import ace_editor

def page_1_2_types_and_values():
    st.title("1.2 Types and Values 🛠")
    st.write('''
    A value is one of the basic things a programme works with, like a letter or a number. Some examples of values are 3, 54.0, and “Hello, World!” 

    These values belong to different types: 
    - 3 is an *integer*
    - 53.0 is a *floating-point number* 
    - “Hello, World!” is a *string* 

    If you are not sure what type a value has, you can find out easily. You just have to write type(), and then the value whose type you want to check inside the parentheses. \n
    E.g. if you want to check the type of 3, write type(2).
    ''')
    st.info(''' **Exercise 1.2.1** \n\n 
    Try checking the types of 3, 53.0 and “Hello World”, in the code window below. \n\n 
    Remember: In order to see the output, you have to use the print function. 
    ''')

    # code window
    ace_editor()

    with st.expander("📖 Press here for help"):
            st.write("""
                Did you write print(type(2))? print(type(42.2))?
                Maybe you forgot a parenthesis? 
            """)

    st.write('''
    In these results, the word “class” is used in the sense of a category; a type is a category of values. 

    Not surprisingly, integers belong to the type *int*, strings belong to *str*, and floating-point numbers belong to *float*. 
    ''')

    st.info(''' **Exercise 1.2.2**
    
    What about values like '3' and '53.0'? 
    
    They look like numbers, but they are in quotation marks like string. 
    
    Try testing the types in the code window below. What do you find? See the result in the dropdown menu below the code window. ''')

    # code window
    ace_editor(key="box2")

    with st.expander("📖 Press here for help"):
        st.write("""
            Did you remember to write the print function around the code? \n 
            Did you remember all parantheses? Quotation marks on both sides of the numbers? \n
            DE.g. print(type(2))? print(type(42.2))? 
        """)
    with st.expander("💡 Press here to see the solution"):
        st.write("""

        """)

    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O’Reilly Media.
    ''')
