import os
import cohere
co=cohere.ClientV2(os.getenv("CO_API_KEY"))

def query_cohere(prompt):
    try:
        response=co.chat(model="command-r-plus-08-2024",
                         messages=[{"role":"user",
                                    "content":prompt}])
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__=="__main__":
    user_input=input("enter your prompt: ")
    print("Response:",query_cohere(user_input))