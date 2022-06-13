import streamlit as st

def page_why_programming():
    st.title("0. Why Programming? 🧩")
    st.write('''
    We all use computers everyday - at home, at school, in our workplace. Programming underlies every aspect, from apps or websites to data analysis or machine learning.


    
    Programming is not only the action of building a program, it also encompasses an understanding of the underlying process. Logical reasoning, good to know.
    Computational thinking.
    
    Computers are continuously becoming a larger part of our daily life, and, consequently, so is digitalisation.
    This is also true for the field of humanities (Karczmarczuk, 2016), for whom learning to program can be a daunting task.
    Accompanying the expanding digitalisation, computer science tools, such as programming, are becoming increasingly ubiquitous.
    Programming involves instructing the computer how to perform a task, using a specific vocabulary and grammatical rules, i.e. a programming language (Kuljis & Baldwin, 2000).
    Natural science students and humanities students usually differ in their approach to programming:
    the former learn the inherent mechanics of these tools, while the latter simply learn how to use them (Karczmarczuk, 2016).
    Programming has a multitude of applications in humanities, including developing databases in history, visual recognition in archaeology, and analytic tools in linguistics (Karczmarczuk, 2016).
    Programming for humanities not only empowers students with universal, generalisable tools, but also provides different and important perspectives to the field of computer science (Karczmarczuk, 2016).
 
    ''')

    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Karczmarczuk, J. (2016). Programming for the Humanities—Logic and Adaptable Languages: Proceedings of the 8th International Conference on Computer Supported Education.
        
        Kuljis, J., & Baldwin, L. P. (2000). Visualisation Techniques for Learning and Teaching Programming. Journal of Computing and Information Technology.
    ''')


    