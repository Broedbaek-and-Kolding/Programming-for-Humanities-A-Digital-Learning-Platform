import streamlit as st
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO

def page_1_how_computers_think():
    #st.markdown(""" <style> .font {
    #    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    #    </style> """, unsafe_allow_html=True)
    #st.markdown('<p class="font">1. How Computers Think </p>', unsafe_allow_html=True)    
    st.title("1. How Computers Think 🧐")
    st.write('''
    By themselves, computers don’t know how to do anything. So, in order for the computer to do what we want them to, we must give them the right instructions. You can think of it like following a recipe: The computer follows the instructions step-by-step to get the outcome we want. 
    
    Much like learning to read, coding can feel hard to learn. The first time you try to code you will, probably, find it difficult, but every time you do it you get better.

    **Natural languages and formal languages** \n
    When giving instructions to the computer, we want to speak a language it understands. In relation to this, it can be useful to discriminate between natural language and formal language. 

    *Natural languages* 
    - are the languages people speak, such as English and Danish. 
    - These languages developed naturally. 

    *Formal languages*
    - are designed for specific applications. 
    - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols. 
    
    Programming languages are formal languages that have been designed to express the computations we want the computer to execute. These languages have strict syntax rules that govern the structure of statements; a kind of grammar. E.g. in mathematics, the statement 3+3=6 follows the correct syntax, while 3+ = 3$6 does not. 

    So, programming languages are a kind of formal language, which we can use to get the computer to behave like we want it to. Unlike when we use natural language to communicate with people, we must tell the computer exactly what to do using a formal language. If you tell a computer to start counting upwards, and don't tell it to stop, it'll keep counting forever! Being a good programmer is all about knowing how to tell a computer to act. (Buckley)

    There are hundreds of different programming languages, which can seem confusing. In this course, we will focus on the language Python.

    In Python, every line of code tells the computer to do something. When we have a document full of code lines, we call it a script. Each script is designed to carry out a job, just like a recipe. 

    **Code Windows** \n
    Throughout this course, there will be exercises to get you started coding. One of the best ways to learn how to code is simply to do it: get it through your hands.  

    Below, you see a box that says “Write code here”. This box runs Python code, when you press the APPLY button just below the box, or CMD+ENTER. \n
    One thing to know about Python is that nothing is returned under “Output of code:” unless you print it. 

    Try to write a calculation below, such as 4+4. What do you get as output? 
    
    Now, try writing print(4+4). Do you get an output now?
    ''')    
    code = st_ace(placeholder='Write code here',language='python',height=50, font_size=16, key="box1")
    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    st.write("Output of code:")
    with stdoutIO() as s:
        try:
            exec(code)
            #st.text("Right now there is no output of your code.")
        except:
            st.warning("Something is wrong with the code.")
            with st.expander("💡 Press here to see the solution"):
                st.write("""
                    If you write 4+4 in the code window above, you don't get an output.
                    To see the result of your calculation, you have to write print() around it. 
                    E.g.  if you write print(4+4), you the output will be 8.
                """)
        
        st.text(str(s.getvalue()))



    