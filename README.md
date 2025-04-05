# RAG Chatbot Website

This website is a retrival augmented generation chatbot. It can be used to answer questions from a custiom knowledge bank
of html, pdf, and txt data.

## Installation Ubuntu

To run this program you'll have python installed on your machine. The installation process is for ubuntu.

### Create a virtual environment

##
        python3 -m venv venv

### Activate the the virtual environment 

##
        source venv/bin/activate

### Install pip packages

##
        pip install langchain_openai langchain_chroma flask html2text langchain_community unstructured

### Run the application

##
        python3 app.py

## Using the program:

1. You need to get an open ai api key and place it inside the quotation marks in the .env file.
2. OPENAI_API_KEY = 'YOUR API KEY GOES HERE'.
3. The files within tools/data/html tools/data/pdf and tools/data/txt are placeholders, replace them with your own files.
4. Note: in order to use data from the data/html directory you need to run tools/html2txt.py. 
5. When running html2txt.py, only add the filenames when prompted, a file path isn't needed.   
6. You get a chroma database after the pip install. To update it with your own data run tools/createDatabase.py.
7. Note: you can guide the chatbot's answers by replacing the text on line 62 of app.py with some custom guidlines. 
7. Now type into the cli "python3 app.py".
8. The application will return a link in the command line interface. 
9. Open the link with a brower of your choice.

