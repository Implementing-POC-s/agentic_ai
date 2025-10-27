from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore 
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

load_dotenv()

client = OpenAI(
     api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
pdf_path= Path(__file__).parent/"nodejs.pdf"
#load this file in python program
# utlity function provided by langchain
loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load()
# loader.load is converting into a single page which is called a page called docs.
print(docs[12])


# split the docs into smaller chunks
text_splitter =RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=400
)
# hey text splitter can u plz splitt document for me and in return this will give u chunks ,,these chunks will be of smaller sixe of 1000,,
# we can do Manually but again langchain gives us the tools to us
chunks = text_splitter.split_documents(documents=docs)

# Vector Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
    )

# Technially i ave my embedding model ready now this embedding model to create embeddings for this chunk and store it in the quadrant db which is vector db.So for that we something known as bridge.So you can see langchain bridge

vector_store= QdrantVectorStore.from_documents(
    # these ar ethe chunks which i want to store
    documents= chunks,
    embedding=embedding_model,
    # this is where my database is ruuning at this port
    url="http://localhost:6333",
    # collection name is basically a logicalSplitting
    collection_name="learning_rag"

)
print("Indexing of documents...")

# 1. took a pdf path
# 2. Load the pdf
# 3. splitted into the chunks
# 4. and we vector embedding that is basically we make vector embedding out of it.
# 5. and then store it in vector db.