import streamlit as st

def page_1_how_computers_think():
    #st.markdown(""" <style> .font {
    #    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    #    </style> """, unsafe_allow_html=True)
    #st.markdown('<p class="font">1. How Computers Think </p>', unsafe_allow_html=True)    
    st.title("1. How Computers Think 🧐")
    st.write('''
    By themselves, computers don't know how to do anything. So, in order for the computer to do what we want them to, we must give them the right instructions. You can think of it like following a recipe: The computer follows the instructions step-by-step to get the outcome we want. 
    
    Much like learning to read, coding can feel hard to learn. The first time you try to code you will, probably, find it difficult, but every time you do it you get better.
    ''')
    st.subheader("Natural languages and formal languages")
    st.write('''
    When giving instructions to the computer, we want to speak a language it understands. In relation to this, it can be useful to discriminate between natural language and formal language. 

    *Natural languages* 
    - are the languages people speak, such as English and Danish. 
    - These languages developed naturally. 

    *Formal languages*
    - are designed for specific applications. 
    - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols. 
    
    Programming languages are formal languages that have been designed to express the computations we want the computer to execute. These languages have strict syntax rules that govern the structure of statements; a kind of grammar. E.g. in mathematics, the statement 3+3=6 follows the correct syntax, while 3+ = 3$6 does not. 

    So, programming languages are a kind of formal language, which we can use to get the computer to behave like we want it to. Unlike when we use natural language to communicate with people, we must tell the computer exactly what to do using a formal language. If you tell a computer to start counting upwards, and don't tell it to stop, it'll keep counting forever! Being a good programmer is all about knowing how to tell a computer to act. 
    ''')

    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Buckley, I. (2019, December 5). What Is Coding and How Does It Work? MUO. https://www.makeuseof.com/tag/what-is-coding/
        
        Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O’Reilly Media.
    ''')


    