from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph,START,END
from openai import OpenAI
import os
  
load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)


# my state has 3 things below

class State(TypedDict):
    user_query: str
    llm_input: Optional[str]
    is_good: Optional[bool]
    llm_output: Optional[str]


def chatbot(state: State):
    print("chatbot Node", state)
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            # read the state
            {"role":"user","content":state.get("user_query")}
        ]
    )

    state["llm_output"]=response.choices[0].message.content
    return state
# redirect
def evaluate_response(state: State) ->Literal["chatbot_gemini","endnode"]:
    print("evaluate_response Node", state)

    if False:
        return "endnode"
    
    return "chatbot_gemini"

def chatbot_gemini(state:State):
    print("chatbot_gemini Node", state)

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            # read the state
            {"role":"user","content":state.get("user_query")}
        ]
    )

    state["llm_output"]=response.choices[0].message.content
    return state
def endnode(state: State):
    print("endnode Node", state)

    return state

graph_builder= StateGraph(State)

# hey graph builder, i want to register the node with yoou

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode",endnode)

# hey graph_builder lets quickly do the add_edge

graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)


graph=graph_builder.compile()

updated_state=graph.invoke(State({"user_query":"HEy,what is 3+3?"}))
print(updated_state)








# # what i ahve done here is:
# # we take the state
# # read the state
# do an llm call
# update the state
# return the state


# if evaluation is not good,,redirect it to the chatbot_gemini node.