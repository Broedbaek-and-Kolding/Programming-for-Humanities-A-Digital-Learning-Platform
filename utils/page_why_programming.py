import streamlit as st

def page_why_programming():
    st.title("0. Why Programming? 🧩")
    st.write('''
    We all use and interact with computers everyday - at home, at school, in our workplace. Programming underlies every aspect of these interactions, from apps or websites to data analysis or machine learning.
    Programming has a multitude of applications in humanities, including developing databases for historians, visual recognition for archaeologists, and analytic tools for linguists.
    However, programming is not only the action of building a program, but also involves an understanding of the underlying process, which necessitates a specific way of thinking and expressing problems. 
    Computational thinking involves thinking about and framing problems and solutions in a way that would also allow a computer to execute them. But it is not only about using programming languages to instruct computers how to solve a problem, but also how computing principles can by used to understand and analyise both natural and artificial processes.
    *lamp picture*
    These skills are essential not only for programming applications, but can aid problem solving in general, across both fields of science and humanities.
    Consequently, these skills can be used not only as a tool for understanding and expressing problems in a way computers can understand, but also as a lens for understanding general problems and interpreting outcomes.

    ''')

    expander = st.expander("Literature")
    expander.write('''
        For this page, we used the following literature: \n 

        Denning, P. J., & Tedre, M. (2021). Computational Thinking: A Disciplinary Perspective. Informatics in Education.
        
        Karczmarczuk, J. (2016). Programming for the Humanities—Logic and Adaptable Languages: Proceedings of the 8th International Conference on Computer Supported Education.
        
        Kuljis, J., & Baldwin, L. P. (2000). Visualisation Techniques for Learning and Teaching Programming. Journal of Computing and Information Technology.
    ''')


    