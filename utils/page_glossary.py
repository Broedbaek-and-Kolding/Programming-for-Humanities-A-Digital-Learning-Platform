import streamlit as st

def page_glossary():
    st.title("1.4 Glossary")
    st.write('''
    
    On this page, you will find an overview of the terms you have learned so far. 

    *Formal languages*
    - Designed for specific applications 
    - Examples: Programming languages or notation in mathematics 
    - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols

    *Natural languages* 
    - The languages people speak, such as English and Danish
    - These languages developed naturally

    *Python*:
    - A programming language 
    ''')

    text_str = '''
    ** 1.4 Glossary **
    
    On this page, you will find an overview of the terms you have learned so far. 

    *Formal languages*
    - Designed for specific applications 
    - Examples: Programming languages or notation in mathematics 
    - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols

    *Natural languages* 
    - The languages people speak, such as English and Danish
    - These languages developed naturally

    *Python*:
    - A programming language 
    '''
    st.download_button('Download glossary', text_str)
'''
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
'''