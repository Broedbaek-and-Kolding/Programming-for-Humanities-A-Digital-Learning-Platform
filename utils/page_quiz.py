import streamlit as st
from  PIL import Image
import os

import numpy as np
import time
import random

def page_quiz():
    # dictionary with questions: [0] = question, 1-3 = answers, 4 = correct answer, 5 = correct feedback, 6 = incorrect feedback
    quiz_dict = {1: ["What does this mean?", "Nothing", "Everything", "Something, but I don't know what", "Everything", "Yes, that is correct, because HCI is LIFE!", "Unfortunately, that is not correct. This is 'everything', because HCI is life"], 
            2: ["Is Sara cool?",'Yes','No','Sometimes', "Yes", "Yes, that is correct! \n Sara is cool because she's got swag!", "Unfortunately, that is not correct. Sara *is* cool!"], 
            3: ['Can Signe be said to have a functioning arm?', 'Yes','No','Sometimes', "Sometimes", "Yes, that is correct! \n\n Signe's arm only works sometimes because it breaks when she doesn't take care of it!", "Unfortunately, that is not correct. Signe's arm only works sometimes."]}


     # define columns 
    col1, col2, col3 = st.columns([0.3,4,0.3])
    col4, col5, col6, col7 = st.columns([0.3,3,1,0.3])


    # present start button and continue to question 1 when pressed
    with col2:
        if 'quiz_started' not in st.session_state: 
            st.session_state.quiz_started = False
            st.title("Welcome to the quiz!")
            st.markdown('''
            In the following quiz, we will review some of the things, you have learned to far.
            
            The quiz contains 10 questions which will be presented one at a time. 

            To continue to the first question, press the button below.

            Enjoy! \n \n

            ''')
        

    # prepare counter for correct questions
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    # show start page 
    with col2: 
        if not st.session_state.quiz_started:
            placeholder_start = st.empty()
            start = placeholder_start.button("Press to start the quiz", key="start")
            if start:
                st.session_state.quiz_started = True
                st.session_state.q_number = 1
    
    placeholder_start = st.empty
    
    # if quiz is started, show questions one by one
    if st.session_state.quiz_started:
        start = st.empty
        q = st.session_state.q_number

        # if last question 
        if q > len(quiz_dict):
            with col2:
                st.header("You have completed the quiz!")
                st.markdown(f'''
                You answered {st.session_state.counter} of {len(quiz_dict)} questions correctly! Well done!
                
                You have received a batch for your first quiz.

                Congratulations!
                ''')
                batchq1 = Image.open(os.path.join(os.path.abspath(""),'images','batchq1.png'))
                st.image(batchq1, width=100)

                st.markdown('''
                To continue to the next topic, and learn even more about programming go to the sidebar \n\n and choose the topic you want to learn more about.''')

                if st.button("Press here to save your batch in the sidebar",key="sidebar_batch"):
                    with st.sidebar:
                        if 'batch' not in st.session_state or st.session_state.batch == "q1":
                            st.session_state.batch = "q1"
                            st.image(batchq1, width=50)
                    st.write("Unfortunately, for now, this batch will disappear when you leave this tab. We are working on how to preserve it!")

        # for q in range(1,len(quiz_dict)+1):
        with col2:
            if q <= len(quiz_dict):
                st.subheader(f"Question {q}/{len(quiz_dict)}")
                
                placeholder = st.empty()
                
                form = placeholder.form(key=f'form{q}')
                form.write('Press submit when you have chosen your answer.')
                radio = form.radio(quiz_dict[q][0],(quiz_dict[q][1],quiz_dict[q][2],quiz_dict[q][3]))
                submit = form.form_submit_button('Submit')

                # if answer is correct
                if submit and radio == quiz_dict[q][4]:
                    st.success(quiz_dict[q][5])
                    st.markdown("Press 'Next Question' to continue to the next question")
                    col6.button("Next Question", key="A"+str(q))
                    # update question number
                    st.session_state.q_number += 1
                    # update correct answer counter
                    st.session_state.counter += 1
                
                # if answer is incorrect
                if submit and radio != quiz_dict[q][4]:
                    st.error(quiz_dict[q][6])
                    st.markdown("Press 'Next Question' to continue to the next question")
                    col6.button("Next Question", key="A"+str(q))
                    # update question number
                    st.session_state.q_number += 1
                
                if st.session_state.q_number > q:
                    placeholder.empty()



    # for q in quiz_dict:
    #     st.write(q)
    #     radio = st.radio(quiz_dict[q][0],(quiz_dict[q][1],quiz_dict[q][2],quiz_dict[q][3]))
    #     if st.button("Submit Answer",key=q): 
    #         if radio == quiz_dict[q][4]:
    #             st.success("Correct!")
    #             if q == 1: 
    #                 st.success("This means everything, because HCI is LIFE!")
    #         else:
    #             st.error("Incorrect. Try again ")
        



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