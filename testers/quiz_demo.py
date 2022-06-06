import streamlit as st
from  PIL import Image
import os

import numpy as np
import time
import random


root_dir = os.path.abspath("")
img = Image.open(os.path.join(root_dir,'images','chcaa_logowithtext.png'))

st.set_page_config(page_icon=img)

quiz_dict = {1: ["What does this mean?", "Nothing", "Everything", "Something, but I don't know what"], 
        2: ["Is Sara cool?",'Yes','No','Sometimes'], 
        3: ['Can Signe be said to have a functioning arm?', 'Yes','No','Sometimes']}


for q in quiz_dict:
    st.radio(quiz_dict[q][0],(quiz_dict[q][1],quiz_dict[q][2],quiz_dict[q][3]))
    if st.button("Submit Answer"): 
        st.write("Answer submitted")
        #st.button()
        


# progress bar 
'''
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)
'''

'''
import streamlit.session_state as session_state
from streamlit.ScriptRunner import RerunException
from streamlit.ScriptRequestQueue import RerunData

state = session_state.get(question_number=0)


@st.cache
def get_question(question_number):
    arr = np.random.randint(0, 100, 2)
    q = f"{arr[0]} * {arr[1]}"
    ans = arr[0]*arr[1]
    choices = ["Please select an answer", ans, ans-1, ans+1, ans+2]
    return arr, q, ans, choices

arr, q, ans, choices = get_question(state.question_number)

st.text(f"Solve: {q}")
a = st.selectbox('Answer:', choices)

if a != "Please select an answer":
    st.write(f"You chose {a}")
    if (ans == a):
        st.write("Correct!")
    else:
        st.write(f"Wrong!, the correct answer is {ans}")

if st.button('Next question'):
    state.question_number += 1
    raise RerunException(RerunData(widget_state=None))
'''