# RAG Chatbot Website

This website is a retrival augmented generation chatbot. It can be used to answer questions from a custiom knowledge bank
of html, pdf, and txt data.

## Installation

To run this program you'll have python installed on your machine.



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
2. OPENAI_API_KEY = 'YOUR API KEY GOES HERE'
3. The files within data/html data/pdf and data/txt are placeholders, replace them with your own files.
4. You get a chroma database after the pip install. To update it with your own data run tools/createDatabase.py.
5. Now type into the cli "python3 app.py".
6. The application will return a link in the command line interface. 
7. Open the link with a brower of your choice.

