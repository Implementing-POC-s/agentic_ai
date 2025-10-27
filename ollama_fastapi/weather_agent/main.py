from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client= OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
def main():
    # take the input from the user
    user_query = input(">")
    # OpenAI client
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        # CHAT-ML prompt
        messages=[
            {"role":"user","content": user_query}
        ]
    )
            
    print(f":{response.choices[0].message.content}")
main()
    

# what we r doing-> 1.Take a n input from user
# 2. make an llm call to gpt
# 3. print the llm response
