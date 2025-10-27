# zero shot prompting->model is direct given task without prior notice.
# # tiktoken hepls to tokenize abd detokenize a text-->use of pip install tiktoken

# import tiktoken 

# enc = tiktoken.encoding_for_model("gpt-4o")
# text ="hey there! my name is sahil"
# tokens = enc.encode(text)
# print("Tokens",tokens)

# # Tokens [48467, 1354, 0, 922, 1308, 382, 18820, 311]

# decoded = enc.decode( [48467, 1354, 0, 922, 1308, 382, 18820, 311])
# print("decoded",decoded)
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client= OpenAI(
api_key= "AIzaSyCUeu-tDvL0mhVPqM53-vx-JbvhPL7c7U0",
# making my call to googleapis
base_url="https://generativelanguage.googleapis.com/v1beta/"
# //using third party gemini compatible endpoint 
)
SYSTEM_PROMPT="You should only and only answer coding realted questions,your name is alexa if user asks any thing other than coding related questions just say sorry"

response=client.chat.completions.create(
    # parameters
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"hey there,can u tell me a joke"}
    ]
)

print(response.choices[0].message.content)



 