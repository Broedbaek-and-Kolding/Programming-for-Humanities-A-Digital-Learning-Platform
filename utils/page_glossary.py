import streamlit as st

def page_glossary():
    st.title("📖 1.4 Glossary")
    st.write("On this page, you will find an overview of the terms you have learned so far. Click the download button below to download them on your computer for later use.")
    text_str = '''

    *Conditional Execution:*
    - One of the few basic instructions that appear in every programming language
    - Check for certain conditions nd run the appropriate code.
        
    *Float:*
    - A type 
    - Short for floating-point number
    - Includes decimal numbers, such as 46.8, 497.3, and 9,0. 

    *Formal languages:*
    - Designed for specific applications
    - Examples: Programming languages or notation in mathematics
    - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols

    *Functions:*
    - Can be thought of as little machines, which you can put something into. Then, they manipulate the input in some way, and, maybe, returns an output.
    - Examples introduced in this course: Print() and type().

    *Input:*
    - One of the few basic instructions that appear in every programming language
    - Get data from the keyboard, a file, the network, or some oher device

    *Int:*
    - A type 
    - Short for integer
    - Includes integers (i.e., numbers with no decimals), such as 4, 7, and 34567.

    *Math:*
    - One of the few basic instructions that appear in every programming language
    - Perform besic mathematical operations, like addition and multiplication

    *Natural languages:*
    - The languages people speak, such as English and Danish
    - These languages developed naturally

    *Output:*
    - One of the few basic instructions that appear in every programming language
    - Display data on the screen, save it in a file, send it over the network, etc.

    *Print() function:*
    - used to display messages on the screen
    - It is called by giving the name of the function, print, followed by a pair of parentheses (brackets) which contain the parameters you want to pass to it.
    - When you use the print function, the parameter you write inside the brackets are the input; it is what you put into the function.
    - The output is the printed text. 

    *Python:*
    - A programming language 
    - A general-purpose language well-suited for many applications, with simple and naturalistic syntax (i.e., "grammar")
    - It is considered easy to use and appropriate for introductory programming
    - Python is free and open source, which means that new modules and functionalities are continuously developed and released.

    Repetition:
    - One of the few basic instructions that appear in every programming language
    - Perform some action repeatedly, usually with some variation

    *Script:*
    - A document full of lines of code 
    - Each script is designed to carry out a job, just like a recipe. 
    - All steps are important and must be written out specifically - and in the right order. 

    *Str:*
    - A type
    - Short for string
    - Includes everything in quotation marks, such as “hello world!”, “43” and “8.3”. 

    *Syntax:*
    - The ”grammar” of a programming language

    *Type() function:*
    - Use the type function, when you are not sure what type a value has
    - E.g. if you want to check the type of 3, write type(2).
    - Remember: If you want the output printed, you have to use the print() function around it. E.g. print(type(2)).
    '''

    # download button
    st.download_button('Download glossary', "**1.4. Glossary**" + text_str)

    # show text
    st.write(text_str)
    
'''
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
'''