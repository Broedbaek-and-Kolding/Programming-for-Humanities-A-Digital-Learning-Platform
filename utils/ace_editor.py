import streamlit as st
from streamlit_ace import st_ace
import contextlib
import sys
from io import StringIO

def ace_editor(key = "box1"):
        # Define code window
    code = st_ace(placeholder='Write code here',language='python',height=100, font_size=16, key=key)

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
            st.warning("Something is wrong with the code. Therefore, you get an error message, which you can see in the red box below. \n\n You will learn about these later - Otherwise, you can try googling what it means (this is what most programmers do!)")
            st.warning("As long as you have an error here, you are not able to go on to the next exercise, or get help for this exercise. \n\n Please, empty the code window and click the APPLY button to continue")
            exec(code)
        
        # Output 
        #st.markdown('<div style="font-size: 20px; padding: 10px; border: 1px solid lightgray; border-radius: 5px; margin: 10px;">' + str(s.getvalue()) + '</div>', unsafe_allow_html=True)
        st.success(str(s.getvalue()))
    
