from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain.chat_models import init_chat_model

load_dotenv()

llm= init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai"
)

# Creating a state(a piece of data and it can be anything)
class State(TypedDict):
    messages: Annotated[list,add_messages]
# i'm creating a chatbot as a node (# Node->the function that does the specific task)and every node has a state 
def chatbot(state: State):
    # print("Inside chatbotnode",state)
    response= llm.invoke(state.get("messages"))

    return {"messages": [response]}

def samplenode(state: State):
    print("\n\nInside  samplenode",state)
    return {"messages":["Sample messages appended"]}

graph_builder= StateGraph(State)

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("samplenode",samplenode)

# currentstate = {messages:["hey there"]}
# node runs: chatbot(state:["hey there"])-> ["hi,this is amessage from chatbot node"]
# state = {"messages":["hey,there","hi,this ia a message from chatbot node"]}

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot","samplenode")
graph_builder.add_edge("samplenode",END)

# on compiling, the graph will run in the abpove sequence order
graph= graph_builder.compile()

updated_state = graph.invoke(State({"messages":["hi,my name is sahil"]}))
print("\n\nupdated_state", updated_state)