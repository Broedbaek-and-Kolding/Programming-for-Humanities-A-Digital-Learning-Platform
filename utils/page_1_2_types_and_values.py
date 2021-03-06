import streamlit as st
import os
from  PIL import Image
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO

from utils.ace_editor import ace_editor

def page_1_2_types_and_values():
    st.title("🛠 1.2 Types and Values")
    # text
    st.write('''
    A *value* is one of the basic things a programme works with, like a letter or a number. Some examples of values are `3`, `53.4`, and `“Hello, World!”`. 

    These values belong to different *types*: 
    - `3` is an *integer*
    - `53.4` is a *floating-point number* (otherwise known as decimal numbers)
    - `“Hello, World!”` is a *string* 

    There are many types in Python, as you can see from the image below. For now, we will focus on integers, floating-point numbers and strings. 
    ''') 
    # image: python data types
    im = Image.open(os.path.join(os.path.abspath(""),'images','python_data_types_newblues.png'))
    st.image(im,use_column_width=True, output_format="PNG")

    st.subheader("The type() function")
    st.write('''
    If you are not sure what type a value has, you can find out easily. You just have to use the type function, and then the value whose type you want to check inside the brackets. \n
    E.g. if you want to check the type of `3`, write `type(3)`.
    
    The output of the type() function looks something like: `<class "int">`, `<class "str">`, or `<class "float">`.
    
    *Class* is used here in the sense of a category; a type is a category of values. 
    
    The next part of the output refers to the type of the value you are checking. Not surprisingly, integers, such as `3`, belong to the type *int*, floating-point numbers, such as `53.4`, belong to the type *float*, and strings, such as `"hello!"`, belong to the type *str*. 
    ''')

    # exercise 1.2.1
    st.info(''' **Exercise 1.2.1** \n\n 
    Try checking the types of `3`, `53.4` and `“Hello World”`, in the code editor below. \n\n 
    Remember: In order to see the output, you have to use the print() function. 
    ''')

    # code editor
    ace_editor()

    # expander: help
    with st.expander("📖 Press here for help"):
        st.write('''
        Did you remember to write the print function around the code? \n 
        
        Did you remember all parantheses? \n
        
        Quotation marks on both sides of the numbers? \n
        
        E.g., `print(type(3))`? Or `print(type(53.4))`? 
        ''')

    # expander: solution
    with st.expander("💡 Press here to see the solution"):
        st.write("""
        To check the type of e.g. `3`, you have to write `print(type(3))` and then run the code by pressing the APPLY button. 
        For `53.4` and `“Hello World”`, you have to write `print(type(53.4))` and `print(type("Hello World"))`. 

        When you check which type 3 is, you get the result: `<class 'int'>`
        
        For 53.4, the result is: `<class 'float'>`
        
        For "Hello World", the result is: `<class 'str'>`
        """)

    st.write('''
    Well done! Hopefully, trying this out gave you a better understanding of how to test the type of a value. 

    In the next exercise, you will learn about something a little bit tricky in Python: how quotation marks can change the type. 
    ''')

    # exercise 1.2.2
    st.info(''' **Exercise 1.2.3**
    
    What type are values like `'3'` and `'53.4'`? 
    
    They look like numbers but are in quotation marks - just like strings. 
    
    Try testing the types in the code editor below. What do you find? See the result in the dropdown menu below the code editor. ''')

    # code editor
    ace_editor(key="box2")

    # expander: help
    with st.expander("📖 Press here for help"):
        st.write('''
            Did you remember to write the print function around the code? \n 
            
            Did you remember all parantheses? Quotation marks on both sides of the numbers? \n
            
            E.g., `print(type(3))`? Or `print(type(53.2))`? 
        ''')
    
    # expander: solution
    with st.expander("💡 Press here to see the solution"):
        st.write("""
        When you write numbers, like `3` and `53.4`, in quotation marks, Python reads them as strings (i.e., the str type). 
        
        Basically, everything you put into quotation marks will be read as strings by Python - even variables that look like numbers!
        """)

    # text: summary
    st.subheader("📋 Summary") 
    st.write('''
    Since this was more technical, here is a summary of what you have learned on this page: 
    - A *value* is one of the basic things a programme works with, like a letter or a number. Some examples of values are `3`, `53.4`, and `“Hello, World!”` 
    - *Integers* are numbers with no decimals, such as `3`, `5`, or `1000`
    - *Floating-point numbers*, or *floats*, are decimal numbers such as `53.4` or `4667.345`
    - *Strings* are values in quotation marks, such as `"Hello, World!"`. Importantly, it also includes values such as `"42"` and `"5.62"` even though they look like integers and floats if they are in quotation marks! 
    - The *type() function* helps you check the type of a value. E.g., if you want to check the type of 3, write `type(3)`.  The output of the type() function looks something like `<class "int">`, `<class "str">`, or `<class "float">`.
    '''
    )

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

            Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O'Reilly Media.

            Python data types (2022), Programmers Portal, https://programmersportal.com/python-data-types/ 
        ''')

    
