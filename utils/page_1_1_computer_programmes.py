import streamlit as st
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO
import os
from  PIL import Image

from utils.ace_editor import ace_editor

def page_1_1_computer_programmes():
    st.title("1.1 Computer Programmes 💻 ")

    st.write('''
    A *programme* is a sequence of instructions that specifies how to perform a computation. 
    The computation might be something mathematical, like solving an equation, but it can also be a symbolic computation, such as searching and replacing text in a document, or something graphhical, like processing an image or playing a video. 

    The details look different in every language, but a few basic instructions appear in just about every language: 

    *Input:* 
    - Get data from the keyboard, a file, the network, or some oher device 

    *Output:* 
    - Display data on the screen, save it in a file, send it over the network, etc. 

    *Math:* 
    - Perform besic mathematical operations, like addition and multiplication 

    *Conditonal Execution:* 
    - Check for certain conditions nd run the appropriate code. 

    *Repetition:* 
    - Perform some action repeatedly, usually with some variation 

    Believe it or not, that's pretty much all there is to it. Every programme you've have used, no matter how complicated, is made up of instruictions that look pretty much like these. 
    So you can think of programming as the process of breaking a large, complex task into smaller and smaller subtasks until the subtasks are simple enough to be performed with one of these basic instructions.
    ''')
    
    st.subheader("Python")    
    st.write(''' 
    There are hundreds of different programming languages, which can seem confusing. In this course, we will focus on the language Python.
    Python is a general-purpose language well-suited for many applications, with simple and naturalistic syntax (i.e., "grammar").
    It is considered easy to use and appropriate for introductory programming.
    Additionally, Python is free and open source, which means that new modules and functionalities are continuously developed and released.
    
    In Python, every line of code tells the computer to do something. When we have a document full of code lines, we call it a *script*. 
    Each script is designed to carry out a job, just like a recipe. And just like a recipe, all steps are important and must be written out specifically - and in the right order. If all steps are written correctly, it can be followed precisely, step by step, to get the cake/the output we want. 
    ''')
    # recipe image
    im = Image.open(os.path.join(os.path.abspath(""),'images','cake_recipe.png'))
    st.image(im,use_column_width=True, output_format="PNG")

    # code editors text
    st.subheader("Code Editors")  
    st.write('''
    Throughout this course, there will be exercises to get you started coding. One of the best ways to learn how to code is simply to do it: get it through your hands.  

    Below, you see a code editor that says “Write code here”. This editor runs Python code, when you press the APPLY button just below the editor, or CMD+ENTER / CTRL+ENTER. \n
    
    One thing to know about Python is that nothing is returned unless you "print" it. Therefore, in these simple scenarios that we will practice, you need to use the print() function. 
    
    
    "What is a function?", you might ask. A *function* can be thought of as little machines, which you can put something into. Then, they manipulate the input in some way, and, maybe, returns an output. 

    For instance , the print function is used to display messages on the screen. It is called by giving the name of the function, print, followed by a 
    pair of parentheses (brackets) which contain the parameters you want to pass to it. On the image below, the string "hello world" is the parameter. 
    ''')

    # print function image
    im2 = Image.open(os.path.join(os.path.abspath(""),'images','print_function_small.png'))
    st.image(im2,use_column_width=True, output_format="PNG")

    # exerciese
    st.info('''
    **Exercise 1.1.1**

    Try to write a calculation in the code editor below, e.g., 4+4. What do you get as output? 
    
    Now, try writing print(4+4). Do you get an output now?
    ''')

    # code editor
    ace_editor()

    # expander: solution
    with st.expander("💡 Press here to see the solution"):
        st.write("""
            If you write 4+4 in the code editor above, you don't get an output. \n 
            To see the result of your calculation, you have to write print() around it. \n 
            E.g.  if you write print(4+4), the output will be 8 - but if you write 4+4, you'll not get an output. 
        """)

    # exmpander: literature
    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Future Learn (n.d.). What is a function? - Using ”Functions” to Code. https://bit.ly/3Hj9tg4

        Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O'Reilly Media.
    ''')
