import streamlit as st

def page_survey():
    st.title("📋 Survey Time!") # ⚙️ 📜 📋 ✏️
    st.markdown('''
    Thank you for completing the course *Python Programming for Humanities*!

    We appreciate it! 

    The last thing, we would like you to do, is to go to the link below and fill out the questionnaire. 
    
    <a href="https://forms.gle/wzmw32YawPdBcHUn8">Questionnaire for Python Programming for Humanities Platform</a>

    Thank you! 

    ''', unsafe_allow_html=True)
    