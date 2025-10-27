#chain of thought prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client= OpenAI(
api_key= "AIzaSyCUeu-tDvL0mhVPqM53-vx-JbvhPL7c7U0",
# making my call to googleapis
base_url="https://generativelanguage.googleapis.com/v1beta/"
# //using third party gemini compatible endpoint 
)

SYSTEM_PROMPT="""

Ypu're an expert ai assistant in resolving user queries using chain of thought
You work on START ,plan and output steps.
you need to first PLAN what needs to bed one.The PLAN can be multiple steps.

Rules:
-strictly folow the given json output format
only run one step at a rime
teh sequence of steps is START(where user gives an input)
"""
response=client.chat.completions.create(
    # parameters
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content": SYSTEM_PROMPT},
        {"role":"user","content":"hey there,can you wrte a code to add n nos in js"}
    ]
)

print(response.choices[0].message.content)
