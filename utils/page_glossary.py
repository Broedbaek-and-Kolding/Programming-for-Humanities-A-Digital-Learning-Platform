import streamlit as st

def page_glossary():
    st.title("📖 1.4 Glossary")
    st.write('''
    On this page, you will find an overview of the terms you have learned so far.

    In the dropdown menu below, you can download the glossary with all terms. If you want to look look up specific terms, choose the terms you want by pressing "Choose an option". You can choose as many as you want. 
    ''')

    with st.expander("Download Glossary"):
        st.write("Click the download button below to download all terms on your computer for later use.")
        # prepare text for download
        text_str = '''

        *Computational Thinking:*
        - Thinking about and framing problems and solutions in a way that would also allow a computer to execute them.
        - How computing principles can by used to understand and analyse both natural and artificial processes.

        *Conditional Execution:*
        - One of the few basic instructions that appear in every programming language
        - Check for certain conditions and run the appropriate code.

        *Float:*
        - A type 
        - Short for floating-point number
        - Includes floating-point numbers, otherwise known as decimal numbers, such as 46.8, 497.3, and 9,0. 

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
    
    # multiselect terms 
    options = st.multiselect(
     'Which terms would you like to look up?',
     ['Computational Thinking', 'Conditional Execution', 'Float', 'Formal languages', 'Functions', 'Input', 'Integer', 'Math', 'Natural languages', 'Output', 'Print() function', 'Python', 'Repetition', 'Script', 'String', 'Syntax', 'Type() function'],
        #default=['Computational Thinking', 'Conditional Execution', 'Float', 'Formal languages', 'Functions', 'Input', 'Integer', 'Math', 'Natural languages', 'Output', 'Print() function', 'Python', 'Repetition', 'Script', 'String', 'Syntax', 'Type() function']
        )
    
    dict = {"Computational Thinking": "*Computational Thinking*: \n - Thinking about and framing problems and solutions in a way that would also allow a computer to execute them. \n - How computing principles can by used to understand and analyse both natural and artificial processes.",
            "Conditional Execution" : "*Conditional Execution:* \n - One of the few basic instructions that appear in every programming language \n - Check for certain conditions and run the appropriate code.",
            "Float" : "*Float:* \n - A type \n - Short for floating-point number \n - Includes floating-point numbers, otherwise known as decimal numbers, such as 46.8, 497.3, and 9,0. ", 
            "Formal languages" : "*Formal languages:* \n - Designed for specific applications \n - Examples: Programming languages or notation in mathematics \n - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols.", 
            "Functions": "*Functions:* \n - Can be thought of as little machines, which you can put something into. Then, they manipulate the input in some way, and, maybe, returns an output. \n - Examples introduced in this course: Print() and type().",
            "Input": "*Input:* \n - One of the few basic instructions that appear in every programming language \n  - Get data from the keyboard, a file, the network, or some oher device.", 
            "Integer": "*Integer* \n - A type \n - 'int' for short \n - Includes integers (i.e., numbers with no decimals), such as 4, 7, and 34567.", 
            "Math": "*Math:* \n - One of the few basic instructions that appear in every programming language \n - Perform besic mathematical operations, like addition and multiplication.", 
            "Natural languages": "*Natural languages:* \n - The languages people speak, such as English and Danish. \n - These languages developed naturally.", 
            "Output": "*Output:* \n - One of the few basic instructions that appear in every programming language \n  - Display data on the screen, save it in a file, send it over the network, etc.", 
            "Print() function": "*Print() function:* \n - used to display messages on the screen. \n - It is called by giving the name of the function, print, followed by a pair of parentheses (brackets) which contain the parameters you want to pass to it. \n  - When you use the print function, the parameter you write inside the brackets are the input; it is what you put into the function. \n - The output is the printed text.", 
            "Python": "*Python:* \n - A programming language \n - A general-purpose language well-suited for many applications, with simple and naturalistic syntax (i.e., 'grammar'). \n - It is considered easy to use and appropriate for introductory programming. \n - Python is free and open source, which means that new modules and functionalities are continuously developed and released.",
            "Repetition": "*Repetition:* \n - One of the few basic instructions that appear in every programming language. \n - Perform some action repeatedly, usually with some variation.", 
            "Script": "*Script:* \n - A document full of lines of code. \n - Each script is designed to carry out a job, just like a recipe. \n - All steps are important and must be written out specifically - and in the right order.", 
            "String": "*String:* \n - A type. \n - 'str' for short. \n - Includes everything in quotation marks, such as 'hello world!', '43' and '8.3'.",
            "Syntax": "*Syntax:* \n - The ”grammar” of a programming language.", 
            "Type() function": "*Type() function:* \n - Use the type function, when you are not sure what type a value has. \n - E.g., if you want to check the type of 3, write type(2). \n - Remember: If you want the output printed, you have to use the print() function around it. E.g. print(type(2))."
        }

    # text of selected terms
    for option in options:
        st.write(dict.get(option))

    # expander terms
    # with st.expander("Computational Thinking"):
    #     st.write('''
    #     - Thinking about and framing problems and solutions in a way that would also allow a computer to execute them.
    #     - How computing principles can by used to understand and analyse both natural and artificial processes.
    #     ''')
    
    # with st.expander("Conditional Execution:"):
    #     st.write('''
    #     - One of the few basic instructions that appear in every programming language
    #     - Check for certain conditions and run the appropriate code.
    #     ''')
    
        # *Float:*
        # - A type 
        # - Short for floating-point number
        # - Includes floating-point numbers, otherwise known as decimal numbers, such as 46.8, 497.3, and 9,0. 

        # *Formal languages:*
        # - Designed for specific applications
        # - Examples: Programming languages or notation in mathematics
        # - For instance, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols

        # *Functions:*
        # - Can be thought of as little machines, which you can put something into. Then, they manipulate the input in some way, and, maybe, returns an output.
        # - Examples introduced in this course: Print() and type().

        # *Input:*
        # - One of the few basic instructions that appear in every programming language
        # - Get data from the keyboard, a file, the network, or some oher device

        # *Int:*
        # - A type 
        # - Short for integer
        # - Includes integers (i.e., numbers with no decimals), such as 4, 7, and 34567.

        # *Math:*
        # - One of the few basic instructions that appear in every programming language
        # - Perform besic mathematical operations, like addition and multiplication

        # *Natural languages:*
        # - The languages people speak, such as English and Danish
        # - These languages developed naturally

        # *Output:*
        # - One of the few basic instructions that appear in every programming language
        # - Display data on the screen, save it in a file, send it over the network, etc.

        # *Print() function:*
        # - used to display messages on the screen
        # - It is called by giving the name of the function, print, followed by a pair of parentheses (brackets) which contain the parameters you want to pass to it.
        # - When you use the print function, the parameter you write inside the brackets are the input; it is what you put into the function.
        # - The output is the printed text. 

        # *Python:*
        # - A programming language 
        # - A general-purpose language well-suited for many applications, with simple and naturalistic syntax (i.e., "grammar")
        # - It is considered easy to use and appropriate for introductory programming
        # - Python is free and open source, which means that new modules and functionalities are continuously developed and released.

        # Repetition:
        # - One of the few basic instructions that appear in every programming language
        # - Perform some action repeatedly, usually with some variation

        # *Script:*
        # - A document full of lines of code 
        # - Each script is designed to carry out a job, just like a recipe. 
        # - All steps are important and must be written out specifically - and in the right order. 

        # *Str:*
        # - A type
        # - Short for string
        # - Includes everything in quotation marks, such as “hello world!”, “43” and “8.3”. 

        # *Syntax:*
        # - The ”grammar” of a programming language

        # *Type() function:*
        # - Use the type function, when you are not sure what type a value has
        # - E.g. if you want to check the type of 3, write type(2).
        # - Remember: If you want the output printed, you have to use the print() function around it. E.g. print(type(2)).
    


def old_page_glossary():
    st.title("📖 1.4 Glossary")
    st.write("On this page, you will find an overview of the terms you have learned so far. \n \n Click the download button below to download them on your computer for later use.")
    text_str = '''

    *Computational Thinking:*
    - Thinking about and framing problems and solutions in a way that would also allow a computer to execute them.
    - How computing principles can by used to understand and analyse both natural and artificial processes.

    *Conditional Execution:*
    - One of the few basic instructions that appear in every programming language
    - Check for certain conditions and run the appropriate code.

    *Float:*
    - A type 
    - Short for floating-point number
    - Includes floating-point numbers, otherwise known as decimal numbers, such as 46.8, 497.3, and 9,0. 

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
   