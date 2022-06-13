import streamlit as st
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO

from utils.ace_editor import ace_editor

def page_1_1_computer_programmes():
    st.title("1.1 Computer Programmes 💻 ")
    
    st.write('''
    There are hundreds of different programming languages, which can seem confusing. In this course, we will focus on the language Python.
    
    In Python, every line of code tells the computer to do something. When we have a document full of code lines, we call it a script. Each script is designed to carry out a job, just like a recipe. 

    **Code Editors** \n
    Throughout this course, there will be exercises to get you started coding. One of the best ways to learn how to code is simply to do it: get it through your hands.  

    Below, you see a code editor that says “Write code here”. This editor runs Python code, when you press the APPLY button just below the editor, or CMD+ENTER / CTRL+ENTER. \n
    One thing to know about Python is that nothing is returned unless you print it. Therefore, in these simple scenarios that we will practice, you need to use the print() function. 
    
    ''')
    st.info('''
    **Exercise**

    Try to write a calculation in the code editor below, e.g., 4+4. What do you get as output? 
    
    Now, try writing print(4+4). Do you get an output now?
    ''')

    ace_editor()
    # # Define code window
    # code = st_ace(placeholder='Write code here',language='python',height=100, font_size=16, key="box1")

    # # Prepare output of code window
    # @contextlib.contextmanager
    # def stdoutIO(stdout=None):
    #     old = sys.stdout
    #     if stdout is None:
    #         stdout = StringIO()
    #     sys.stdout = stdout
    #     yield stdout
    #     sys.stdout = old
    #     #print("stdout:",stdout,sys.stdout,old)

    # st.write("Output of code:")
    # with stdoutIO() as s:
    #     try:
    #         exec(code)
    #         #st.text("Right now there is no output of your code.")
    #     except:
    #         st.warning("Something is wrong with the code. \n Below, in the red box, you can see an error message. \n You will learn about these later - Otherwise, try to googling what it means (this is what most programmers do!)")
    #         exec(code)
        
    #     # Output 
    #     st.markdown('''<div 
    #     style="
    #     font-size: 20px; 
    #     padding: 10px; 
    #     border: 1px solid lightgray; 
    #     border-radius: 5px;">\n''' + str(s.getvalue()) +
    #     '''\n </div>''', unsafe_allow_html=True)

    with st.expander("💡 Press here to see the solution"):
        st.write("""
            If you write 4+4 in the code editor above, you don't get an output.
            To see the result of your calculation, you have to write print() around it. 
            E.g.  if you write print(4+4), you the output will be 8.
        """)
