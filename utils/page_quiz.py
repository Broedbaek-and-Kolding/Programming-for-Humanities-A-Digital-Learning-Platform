import streamlit as st
from  PIL import Image
import os

import numpy as np
import time
import random

def page_quiz():
    # dictionary with questions: [0] = question, 1-3 = answers, 4 = correct answer, 5 = correct feedback, 6 = incorrect feedback
    quiz_dict = {1: ["**What type of language is a programming language, such as Python?**", "A natural language", "An informal language","A formal language", "A formal language", "Yes, that is correct! \n\n Programming languages are formal languages because they are specifically designed to express the computations, we want the computer to execute.", "That is not correct, unfortunately. \n\n Programming languages are formal languages because they are specifically designed to express the computations, we want the computer to execute."],
            2: ["**What is the output of this code `4+4`?**", "Nothing", "4+4", "8", "Nothing", "Yes, that is correct! \n\n There will be no output of this code, because the print function is not around the expression. To get an output, the code should be  `print(4+4)`", "That is not correct, unfortunately. \n\n There will be no output of this code, since the print function is not around the expression. To get an output, the code should be  `print(4+4)`"], 
            3: ['**What is computional thinking?**','Thinking like a computer','The way computers think about problems','Framing problems in a way that allows computers to execute them','Framing problems in a way that allows computers to execute them','Correct! \n\n Computational thinking includes framing problems and solutions in a way that would also allow a computer to execute them. \n\n Furthermore, it involves how computing principles can by used to understand and analyse both natural and artificial processes.','That is not correct, unfortunately! \n\n Computational thinking includes framing problems and solutions in a way that would also allow a computer to execute them. \n\n Furthermore, it involves how computing principles can by used to understand and analyse both natural and artificial processes.'],
            4: ["**Which functions have you learned so far?**",'Type() and print()','Print() and conditional execution()','Math() and type()', "Type() and print()", "Yes, that is correct! \n\n `Type()` and `print()` are both functions, which take an input and returns an output. \n\n *Conditional execution* and *math* are some of the basic instructions that appear in almost every programming language.", "Unfortunately, that is not correct. \n\n *Conditional execution* and *math* are some of the basic instructions that appear in almost every programming language. \n\n  `Type()` and `print()`, on the other hand, are functions, which take an input and returns an output."], 
            5: ['**What are some of the advantages of Python?**', "It has simple, naturalistic syntax, and it's free and open source",'It has rich interfaces and server load.','It has static libraries and helps you get hands-on with low-level programming concepts.', "It has simple, naturalistic syntax, and it's free and open source", "Yes, that is correct! \n\n Python has simple, naturalistic syntax, which makes is a great introductory programming language. \n\n Furthermore, and it's free and open source, which means that new modules and functionalities are continuously developed and released.", "Unfortunately, that is not correct. \n\n The advantages of Python include simple, naturalistic syntax, as well as it being free and open source. The naturalistic syntax makes it a great introductory programming language, and, the fact that it is open source means that new modules and functionalities are continuously developed and released. \n\n Rich interfaces, server load, static libraries, as well as hands-on experience with low-level programming concepts are advantages of other programming languages."],
            6: ['**What is the output of this code `print(type(76.0))`**',"<class 'float'>","<class 'str'>","<class 'int'>","<class 'float'>",'Correct! \n\n Decimal numbers, such as 76.0, are called floating-point numbers. When we use the type function to test the type, it is shortened to "float".','That is not correct. \n\n Decimal numbers, such as 76.0, are called floating-point numbers. When we use the type function to test the type, it is shortened to "float". \n\n "int" is short for integer, such as 76, while "str" is short for string, such as "hello!"'],
            7: ['**Why can programming be thought of as a Swiss Army Knive?**','Because it has many functions and applications','Because it is sharp','Because it is powerful and portable','Because it has many functions and applications','Correct! \n\n  Programming is an almost universal tool, that can be thought of as a Swiss Army Knife, with a multitude of functions and applications.','Incorrect! \n\n  Programming can be thought of as a Swiss Army Knife because it is an almost universal tool with a multitude of functions and applications.'],
            8: ['**What is `print()`**','A script','An input','A function','A function','Correct! \n\n `Print()` is a function that prints takes an input and prints it.','That is not correct. \n\n Print() is a *function* that prints takes an *input* and prints it. \n\n A *script* is a document full of code lines.'],
            9: ["**What will happen if you tell a computer to count upwards and don't tell it to stop?**",'It will stop when it reaches 100','It will count until it gets tired','It will keep counting forever','It will keep counting forever',"Correct! \n\n It will count forever, if you haven't told it to stop. \n\n Therefore, we must tell the computer exactly what to do - just like a recipe.","Incorrect! \n\n The computer will count forever, if you haven't told it to stop. \n\n Therefore, we must tell the computer exactly what to do - just like a recipe."],
            10: ['**What type is `"42"`?**','A string','A float','An integer','A string',"Correct! Well done! \n\n Since `'42'` is in quotation marks, it is actually a string! \n\n If `'42'` was not in quotation marks, it would have been an *integer*, since it is not a decimal number (i.e., a *float*)",'Incorrect! \n\n Since `"42"` is in quotation marks, it is actually a string! \n\n If `"42"` was not in quotation marks, it would have been an *integer*, since it is not a decimal number (i.e., a *float*)']}

     # define columns 
    col1, col2, col3 = st.columns([0.3,4,0.3])
    col4, col5, col6, col7 = st.columns([0.3,3,1,0.3])

    # present start button and continue to question 1 when pressed
    with col2:
        if 'quiz_started' not in st.session_state or st.session_state.quiz_started == False: 
            st.session_state.quiz_started = False
            st.title("📣 Welcome to the quiz!") # ⚡️ 📯 🗯 📣 ⚜️ 🌟 ⚡️ 🥇 🏅  🎖 🏆 🥇🥈🥉
            st.markdown('''
            In the following quiz, we will review some of the things, you have learned to far, as well as apply it to new examples!
            
            The quiz contains 10 questions which will be presented one at a time. After you have completed the quiz, you will get a badge - and depending on how well you do, it will be bronze 🥉, silver 🥈 or gold 🥇.  

            To continue to the first question, press the button below.

            NB You might have to double click on the button for this page to disappear. We apologise for the inconvenience! 

            Enjoy!
            ''')
        

    # prepare counter for correct questions and badge for when quiz is completed 
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    if 'badge' not in st.session_state:
        st.session_state.badge = False

    # show start page (start button issue not solved)
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

        # if after last question 
        if q > len(quiz_dict):
            with col2:
                st.header("You have completed the quiz!")
                st.markdown(f'''
                You answered {st.session_state.counter} of {len(quiz_dict)} questions correctly! Well done!
                
                You have received a badge for your first quiz.

                Congratulations!
                ''')
                if st.session_state.counter <= 6:
                    badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_bronze.png'))
                elif 6 < st.session_state.counter <= 8:
                    badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_silver.png'))
                elif st.session_state.counter > 8:
                    badge1 = Image.open(os.path.join(os.path.abspath(""),'images','badge_gold.png'))
                
                st.image(badge1, width=100)

                st.write("NB You might have to double click on the button for the badge to appear in the sidebar. We apologise for the inconvenience.")                

                if st.button("Press here to save your badge in the sidebar",key="sidebar_badge"):
                #     with st.sidebar:
                    st.session_state.badge = "q1"
                            #st.image(badge1, width=50)
                
                
                st.markdown('''
                This was everything from this module! 

                Thank you for completing it.  
                
                To see an overview of all the terms you have learned so far, go to the Glossary tab.''')

        with col2:
            if q <= len(quiz_dict):
                st.subheader(f"Question {q}/{len(quiz_dict)}")
                placeholder = st.empty()
                
                # Make form                
                form = placeholder.form(key=f'form{q}')
                form.write(quiz_dict[q][0])
                radio = form.radio('',(quiz_dict[q][1],quiz_dict[q][2],quiz_dict[q][3]))
                form.write('Press submit when you have chosen your answer.')
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


    # return how many questions were answered correctly and the badge 
    return (st.session_state.counter, st.session_state.badge)


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