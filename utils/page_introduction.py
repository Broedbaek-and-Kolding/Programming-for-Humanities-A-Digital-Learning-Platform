import streamlit as st
import os
from  PIL import Image

def page_intro():
    st.subheader("Welcome to")
    st.header("*Python Programming for Humanities*")
    # text
    st.write('''
    This is a prototype of an online learning platform created as an exam project for the course human-computer interaction on the Cognitive Science master's degree at Aarhus University. 

    In this prototype, we introduce one module, *Python Programming for Humanities*. 
    This module is meant to be a gentle introduction to programming for students with no previous programming experience. 
    ''')
    st.write('''
    We take it one step at a time, with short and interactive exercises to learn about some of the general principles of how programming can be used to work with data. 
    Examples of different types of data used in humanities fields could be surveys, social media posts, literary texts, or historical newspapers.  

    We want to help you get familiar with some programming techniques to help you produce readable and reproducible code, by introducing you to some of the basics of how programming can be used to communicate with computers. 
    
    Below, you see an example of code written in the programming language, Python:
    ''')
    # image
    im = Image.open(os.path.join(os.path.abspath(""),'images','python_code.png'))
    st.image(im, output_format="PNG")
    st.write("Output of code:")
    im2 = Image.open(os.path.join(os.path.abspath(""),'images','python_output.png'))
    st.image(im2, output_format="PNG")
    
    # info box with prerequisites
    st.info(''' **Prerequisites**

    There are no prerequisites for this module. All topics will be explained at an introductory level, and you will try to program in this code windows within this browser without the need to install anything on your computer. 
    ''') 

    # info box with learning oucomes
    st.info(''' **Learning Outcomes**

    Through this module, you will: 
    - Discover the strengths of programming as a tool for humanities 
    - Understand simple computational thinking steps and how they can be applied to problem-solving tasks
    - Understand and apply the concept of types and values
    - Create strings, integers, and floats
    - Check what type a value is
       ''')
    
    # expander with literature
    with st.expander("Literature"):
        st.write('''
            For this platform, we used the following literature: \n 

            Buckley, I. (2019, December 5). What Is Coding and How Does It Work? MUO. https://www.makeuseof.com/tag/what-is-coding/
            
            Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O'Reilly Media.
        ''')

    # text
    st.markdown('''
    You can navigate the module by clicking on the topics in the sidebar on the left, when you want to continue to the next page.  

    We hope that you will learn some new and exciting things about programming! 

    <div style="text-align: right"> Sara Kolding and Signe Kirk Br??db??k </div>
    <div style="text-align: right"> Cognitive Science Graduate Students, Aarhus University </div>
    <div style="text-align: right"> June 10, 2022</div>
    ''',unsafe_allow_html=True)


def page_intro_da():
    st.subheader("Velkommen til")
    st.header("*Programming for Humaniorastuderende i Python*")
    # text
    st.write('''
    Dette er en prototype af en online l??ringsplatform lavet i forbindelse med et eksamensprojekt i faget human-computer intercation p?? kandidatuddannelsen Kognitionsvidenskab p?? Aarhus Universitet.

    Denne prototype inkluderer et modul, *Programmering for Humaniorastuderende i Python*. 

    Dette modul er en introduktion til programmering for studerende, som ikke har erfaring med programmering. 
    ''')
    st.write('''
    Vi tager det ??t step af gangen med korte og interaktive ??velser, s?? du kan l??re nogle generelle principper om, hvordan programmering kan blive brugt til at arbejde med data relevant for humaniora.

    Eksempler p?? datatyper brugt i humaniora kunne v??re sp??rgeskemaunders??gelser, opslag p?? sociale medier, liter??re tekster eller historiske aviser.  

    Vi vil hj??lpe dig med at skifte bekendtskab med nogle programmeringsteknikker til at hj??lpe dig med at skrive l??selig og reproducerbar kode. Derudover kommer til du til at l??re lidt om, hvordan programmering kan bruges til at kommunikere med computere.
    
    Nedenfor kan du se et eksampel p?? kode skrevet i programmeringssproget Python: 
    ''')
    # image
    im = Image.open(os.path.join(os.path.abspath(""),'images','python_code.png'))
    st.image(im, output_format="PNG")
    st.write("Output of code:")
    im2 = Image.open(os.path.join(os.path.abspath(""),'images','python_output.png'))
    st.image(im2, output_format="PNG")
    
    # info box with prerequisites
    st.info(''' **Foruds??tninger**

    Der er ikke nogen foruds??tninger for dette modul. Alle emner vil blive forklaret p?? et introducerende niveau, og du vil pr??ve at programmere i kode editor i denne platform, s?? du ikke beh??ver at installere noget p?? din computer.
    ''') 

    # info box with learning oucomes
    st.info(''' **L??ringsudbytte**

    I dette modul vil du: 
    - Opdage styrkerne ved at bruge programmering som et v??rkt??j i humaniora.
    - Forst?? simple "computational thinking" steps og hvordan de kan blive brugt til probleml??sning
    - Forst?? og anvende koncepterne af typer og v??rdier
    - Lave "strings", "intergers" og "floating-point numbers"
    - Tjekke hvilken type en v??rdi er
       ''')
    
    # expander with literature
    with st.expander("Literatur"):
        st.write('''
            I denne platform, blive f??lgende literatur anvendt: \n 

            Buckley, I. (2019, December 5). What Is Coding and How Does It Work? MUO. https://www.makeuseof.com/tag/what-is-coding/
            
            Downey, A. (2016). 1. The Way of the Program. In Think Python (2nd edition, updated for Python 3). O'Reilly Media.
        ''')

    # text
    st.markdown('''
    Du kan navigere modulet ved at klikke p?? emnerne i menuen til venstre, n??r du vil forts??tte til den n??ste side. 

    Vi h??ber at du kommer ti at l??re nogle nye og sp??ndende ting om programmering i Python!

    <div style="text-align: right"> Sara Kolding og Signe Kirk Br??db??k </div>
    <div style="text-align: right"> Kognitionsvidenskabsstuderende (cand.it.), Aarhus Universitet </div>
    <div style="text-align: right"> 10. juni, 2022</div>
    ''',unsafe_allow_html=True)




## OLD ##
''' **Learning Outcomes**

    At the end of this module, you will have gained knowledge of:    

    *Knowledge*
    - Computational Thinking steps and how they can be applied to problem-solving tasks
    - A range of programming paradigms and their effectiveness for a particular problem
    - The concept of variables and structures for different data types
    - Syntax of computer programming languages, including functions and scripts
    - Boolean Logic, control flow, and looping
    
    During the module, you will obtain skills in order to:

    *Skills*
    - Create and manipulate number sequences, vectors and matrices
    - Create and index matrices and other data types
    - Visualize using data plotting functions
    - Use conditional reasoning to write loops
    - Read, write and save files and explain the difference between different file types
    - Identify the type and dimensionality of new data
    
    You will gain the following competencies through the module:

    *Competencies*
    * Recognize strengths of Python as a programming and environment
    * Implement algorithms in Python code, which manipulate data and visualize results
    '''