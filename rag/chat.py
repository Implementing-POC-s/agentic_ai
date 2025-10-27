from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore 
from openai import OpenAI
import os
load_dotenv()
client = OpenAI(
     api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# Vector Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
    )
# User query needs to be embedded using the same model
# I'm just making a connection, its basically just your embedding model

# now we need a connection to the vector database.,we r picking from the existing colection as we donot store anything 
vector_db=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    # this is the collection we want to query
    collection_name="learning_rag",
    embedding= embedding_model,
)


#Take user input
user_query=input("ask something:")
# Relevant chunks from the vector db what user is asking for
search_results=vector_db.similarity_search(query=user_query)


context= "\n\n\n".join([f"Page Content:{result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location:{result.metadata['source']}"
for result in search_results ])
SYSTEM_PROMPT= f"""

you are a helpful ai  asssitant  who answers user query based on the available context
retrieved from a pdf file along with page_contents and page number.

You should only answer the user based on the following context and naigate the 
user to open the right page number to know more.
 
Context
{context}

"""
response= client.chat.completions.create(
model="gemini-2.5-flash",
messages=[
    {"role":"system","content":SYSTEM_PROMPT},
    {"role":"user","content":user_query}
]
)
print(f":{response.choices[0].message.content}")


# Create vector embeddings,then go into the database .seasrch for it, and then come back and do the retrieval

# 1.Take the user_query
# 2.Create vector embeddings
# 3.Do a similarity search,Along with the relavant chunks,we call the model and do the chatting bussiness.