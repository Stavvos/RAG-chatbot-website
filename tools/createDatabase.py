from langchain_community.document_loaders import PyPDFDirectoryLoader, TextLoader
from langchain_community.document_loaders.merge import MergedDataLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
from langchain_community.document_loaders import DirectoryLoader

# import the .env file
from dotenv import load_dotenv
load_dotenv()

# configuration
PDF_DATA_PATH = r"data/pdf"
CHROMA_PATH = r"../chroma_db"

# initiate the embeddings model
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# initiate the vector store
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

# loading the PDF and TXT documents
pdf_loader = PyPDFDirectoryLoader(PDF_DATA_PATH)
#txt_loader = TextLoader(TXT_FILE_PATH)
txt_loader = DirectoryLoader("./data/txt", glob="**/*.txt")

# Combine loaders
merged_loader = MergedDataLoader(loaders=[txt_loader, pdf_loader])

raw_documents = merged_loader.load()

# splitting the document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

# creating the chunks
chunks = text_splitter.split_documents(raw_documents)

# creating unique ID's
uuids = [str(uuid4()) for _ in range(len(chunks))]

# adding chunks to vector store
vector_store.add_documents(documents=chunks, ids=uuids)
