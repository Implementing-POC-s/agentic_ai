from fastapi import FastAPI,Body
from ollama import Client
# create an application instance using fastapi class
app=FastAPI()
# //making a call to ollama fast api
client = Client(
    host="http://localhost:11434",
    # we can also pass headers
)

# Create an api route
@app.get("/contact-us")
def func_root():
    return {"email":"sahil@kawatra.com"}
# //we need to register it also via post route
@app.post("/chat")
def chat(
        message:str = Body(...,description="the message")
):
    # making an api call to the models locally
    response =client.chat(model="gemma:2b",messages=[
        {"role":"user" , "content": message}
    ])

    return {"response": response.message.content}


    