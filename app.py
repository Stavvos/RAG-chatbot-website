from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv #new

from flask import Flask, render_template, request, jsonify

#configuration
load_dotenv()
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# initiate the model
llm = ChatOpenAI(temperature=0.5, model='gpt-4o-mini')

# connect to the chromadb
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

# Set up the vectorstore to be the retriever
num_results = 5
retriever = vector_store.as_retriever(search_kwargs={'k': num_results})


app = Flask(__name__)

# Serve index.html from the templates folder
@app.route('/')
def home():
    return render_template('index.html')

# Handle the chat messages via POST
@app.route('/chat', methods=['POST'])
def chat():
    
    user_message = request.json.get('message')
    
    if user_message:
        bot_response = generate_bot_response(user_message)
        return {'reply': bot_response.content}

def generate_bot_response(message):

    # retrieve the relevant chunks based on the question asked
    docs = retriever.invoke(message)

    # add all the chunks to 'knowledge'
    knowledge = ""

    for doc in docs:
        knowledge += doc.page_content+"\n\n"


    # make the call to the LLM (including prompt)
    if message is not None:

        rag_prompt = f"""

        If you are unsure about an answer say 'Sorry i don't know the answer to your question'

        The question: {message}

        The knowledge: {knowledge}

        """
        response = llm.invoke(rag_prompt)
        return response
    
    return "Chatbot is offline"

if __name__ == '__main__':
    app.run(debug=True)
