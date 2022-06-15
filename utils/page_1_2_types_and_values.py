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
    # text
    st.write('''
    A value is one of the basic things a programme works with, like a letter or a number. Some examples of values are 3, 53.4, and “Hello, World!” 

    These values belong to different *types*: 
    - 3 is an *integer*
    - 53.4 is a *floating-point number* 
    - “Hello, World!” is a *string* 

    There are many types in Python, as you can see from the image below. For now, we will focus on integers, floating-point numbers and strings. 
    ''') 
    # image: python data types
    im = Image.open(os.path.join(os.path.abspath(""),'images','python_data_types.png'))
    st.image(im,use_column_width=True, output_format="PNG")


    st.write('''
    If you are not sure what type a value has, you can find out easily. You just have to use the type function, and then the value whose type you want to check inside the brackets. \n
    E.g. if you want to check the type of 3, write type(3).
    ''')
    st.info(''' **Exercise 1.2.1** \n\n 
    Try checking the types of 3, 53.4 and “Hello World”, in the code window below. \n\n 
    Remember: In order to see the output, you have to use the print function. 
    ''')

    # code window
    ace_editor()

    # expander: help
    with st.expander("📖 Press here for help"):
            st.write('''
            Did you remember to write the print function around the code? \n 
            
            Did you remember all parantheses? \n
            
            Quotation marks on both sides of the numbers? \n
            
            E.g., print(type(3))? print(type(53.2))? 
            ''')

    st.write('''
    In these results, the word *class* is used in the sense of a category; a type is a category of values. 

    Not surprisingly, integers, such as 3, belong to the type *int*, strings, such as "hello!", belong to *str*, and floating-point numbers, such as 53.4, belong to *float*. 
    ''')

    st.info(''' **Exercise 1.2.2**
    
    What about values like '3' and '53.4'? 
    
    They look like numbers, but they are in quotation marks like string. 
    
    Try testing the types in the code window below. What do you find? See the result in the dropdown menu below the code window. ''')

    # code window
    ace_editor(key="box2")

    # expander: help
    with st.expander("📖 Press here for help"):
        st.write('''
            Did you remember to write the print function around the code? \n 
            
            Did you remember all parantheses? \n
            
            Quotation marks on both sides of the numbers? \n
            
            E.g., print(type(3))? print(type(53.2))? 
        ''')
    
    # expander: solution
    with st.expander("💡 Press here to see the solution"):
        st.write("""
        When you write numbers, like 3 and 53.4, in quotation marks, Python reads them as strings (i.e., the str type). 
        
        Basically, everything you put into quotation marks will be read as strings by Python - even variables that look like numbers!
        """)

    # text
    st.write('''
    This was everything we had for you in this module! Well done! 

    In the next tab, you will find a quiz that will help you revise the knowledge you have just acquired and  apply it to new examples. 

    '''
    )

    # expander: literature
    with st.expander("Literature"):
        st.write('''
            For this page, we used the following literature: \n 

            Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O’Reilly Media.
        ''')
