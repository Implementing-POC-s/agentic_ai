from dotenv import load_dotenv
from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore 
import os

load_dotenv()
client = OpenAI(
     api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

def process_query(query: str):
    # user will  be giving me the query and i will do the retrieval phase
    print("searching Chunks", query)
    search_results = vector_db.similarity_search(query=query)
    
    context = "\n\n\n".join([
        f"Page Content:{result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location:{result.metadata['source']}"
        for result in search_results
    ])

    SYSTEM_PROMPT = f"""
    you are a helpful ai assistant who answers user query based on the available context
    retrieved from a pdf file along with page_contents and page number.

    You should only answer the user based on the following context and navigate the 
    user to open the right page number to know more.
    
    Context
    {context}
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    print(f":{response.choices[0].message.content}")
