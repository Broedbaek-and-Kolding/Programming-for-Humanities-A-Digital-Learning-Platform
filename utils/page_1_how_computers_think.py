import streamlit as st

def page_1_how_computers_think():
    #st.markdown(""" <style> .font {
    #    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    #    </style> """, unsafe_allow_html=True)
    #st.markdown('<p class="font">1. How Computers Think </p>', unsafe_allow_html=True)    
    st.title("1. How Computers Think 🧐")
    st.write('''
    By themselves, computers don't know how to do anything. So, in order for the computer to do what we want them to, we must give them the right instructions. You can think of it like following a recipe: The computer follows the instructions step-by-step to get the outcome we want. Just like when cooking, the order of the steps is important. For example, we can't mix the ingredients properly when we have already baked the cake.
    
    Much like learning to read, learning to program can feel difficult. The first time you try to program you will, probably, find it hard, but it will get easier with practice.
    ''')
    st.subheader("Natural languages and formal languages")
    st.write('''
    Computers do not communicate in the same way that we do. So when giving instructions to the computer, we need to speak a language the computer understands. To understand the difference between communicating with people and communicting with computers, it can be useful to discriminate between natural languages and formal languages. 

    *Natural languages* 
    - are the languages people speak with each other, such as English and Danish. 
    - develop naturally over time. 

    *Formal languages*
    - are designed for specific applications, such as computer programming or mathematics. 
    
    Programming languages are formal languages that have been designed to express the computations we want the computer to execute. These languages have strict syntax rules that govern the structure of statements; a kind of grammar. E.g. in mathematics, the statement 3+3=6 follows the correct syntax, while 3+ = 3$6 does not. There are many different programming languages, and just like natural languages, some of them resemble each other closely while others don't. However, though most of these languages are suited for specific tasks, there are some universal similarities between them, as we will soon see.

    Unlike when we use natural language to communicate with people, we must be very specific when telling the computer what to do using programming languages. If you tell a computer to start counting upwards, and don't tell it to stop, it'll keep counting forever! A big part of learning how to program is learning how to best instruct the computer using a programming language.
    ''')

    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Buckley, I. (2019, December 5). What Is Coding and How Does It Work? MUO. https://www.makeuseof.com/tag/what-is-coding/
        
        Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O’Reilly Media.
    ''')


    