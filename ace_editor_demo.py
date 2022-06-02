"""
In terminal:
- cd ..
- source hci_env/bin/activate
- cd _hci_exam/
- streamlit run streamlit run ace_editor_demo.py 

to stop: control + c
"""

import streamlit as st
from streamlit_ace import st_ace
import sys
from io import StringIO
import contextlib

# setup page
st.set_page_config(page_title="Scientific Programming Learning Module", page_icon = "🧘")
st.title("Scientific Programming Learning Module")

# Spawn a new Ace editor
content = st_ace(placeholder='Write code here',language='python')

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

code = content
# code = """
# i = [0,1,2]
# for j in i :
#     print(j)
# """
st.text("Output of code:")
with stdoutIO() as s:
    try:
        exec(code)
    except:
        #print("Something wrong with the code")
        st.warning("Something is wrong with the code. Click the button below for a hint")

st.text(str(s.getvalue()))


# if content: 
#     if NameError:
#         st.warning("You made a mistake! Try again")
#     c = exec(content)
#     st.text(content)
#     st.text(c)


#calculator
# a = eval(content)

# if content:
#     st.text(str(a))
#     print(type(content))
