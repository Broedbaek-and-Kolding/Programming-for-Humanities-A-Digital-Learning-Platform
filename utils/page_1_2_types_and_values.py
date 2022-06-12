import streamlit as st
import os
from  PIL import Image
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO



def page_1_2_types_and_values():
    st.title("1.2 Types and Values")
    st.write('''
    A value is one of the basic things a programme works with, like a letter or a number. Some examples of values are 2, 42.0, and “Hello, World!” 

    These values belong to different types: 
    - 2 is an *integer*
    - 42.0 is a *floating-point number* 
    - “Hello, World!” is a *string* 

    If you are not sure what type a value has, the code windows can tell you. You just have to write type() and then the value whose type you want to check inside the parentheses, e.g. if you want to check the type of 2, write type(2).

    For example, try to check the types of 2, 42.0 and “Hello World”, in the code window below. \n
    Remember: In order to see the output, you have to use the print function. 
    ''')

    # Define code window
    code = st_ace(placeholder='Write code here',language='python',height=100, font_size=16, key="box1")

    # Prepare output of code window
    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old
        #print("stdout:",stdout,sys.stdout,old)

    st.write("Output of code:")
    with stdoutIO() as s:
        try:
            exec(code)
            #st.text("Right now there is no output of your code.")
        except:
            st.warning("Something is wrong with the code. Below, in the red box, you can see an error message. You will learn about these later.")
            with st.expander("💡 Press here to see the solution"):
                st.write("""
                    Did you write print(type(2))? print(type(42.2))?
                    Maybe you forgot a parenthesis? 
                """)
            exec(code)
        
        # Output 
        st.markdown('''<div 
            style="
            font-size: 20px; 
            padding: 10px; 
            border: 1px solid lightgray; 
            border-radius: 5px;
            margin: 10px;">\n''' + str(s.getvalue()) +
            '''\n </div>''', unsafe_allow_html=True)

        #st.markdown(str(s.getvalue()))    


    st.write('''
    In these results, the word “class” is used in the sense of a category; a type is a category of values. 

    Not surprisingly, integers belong to the type int, strings belong to str, and floating-point numbers belong to float. 
    ''')

    st.info(''' What about values like '2' and '42.0'? They look like numbers, but they are in quotation marks like string. 

    Try testing the types in the code window below. What do you find? See the result in the dropdown menu below the code window. ''')

    # Define code window
    code2 = st_ace(placeholder='Write code here',language='python',height=100, font_size=16, key="box2")

    # Prepare output of code window<
    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old
        #print("stdout:",stdout,sys.stdout,old)

    st.write("Output of code:")
    with stdoutIO() as s:
        try:
            exec(code2)
            #st.text("Right now there is no output of your code.")
        except:
            st.warning('''Something is wrong with the code. Did you write print(type('2'))? \n
            Below, in the red box, you can see an error message. You will learn about these later.''')
            with st.expander("💡 Press here to see the solution"):
                st.write("""
                

                """)
            exec(code2)
        
        # Output 
        st.markdown('''<div 
            style="
            font-size: 20px; 
            padding: 10px; 
            border: 1px solid lightgray; 
            border-radius: 5px;
            margin: 10px;">\n''' + str(s.getvalue()) +
            '''\n </div>''', unsafe_allow_html=True)

    with st.expander("📖 Press here for help"):
                st.write("""
                    Did you remember to write the print function around the code? \n 
                    Did you remember all parantheses? Quotation marks on both sides of the numbers? \n
                    DE.g. print(type(2))? print(type(42.2))? 
                """)
    with st.expander("💡 Press here to see the solution"):
                st.write("""
                    
                    Did you write print(type(2))? print(type(42.2))?
                    Maybe you forgot a parenthesis? 
                """)