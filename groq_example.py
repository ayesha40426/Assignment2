import os
from groq import Groq

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"user","content":prompt}
            ])
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{str(e)}"

if __name__=="__main__":
    user_input=input("enter your prompt: ")
    print("response:",query_groq(user_input))