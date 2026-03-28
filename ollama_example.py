import requests

def query_ollama(prompt):
    try:
        response=requests.post("http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            })
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__=="__main__":
    user_input=input("enter your prompt: ")
    print("response:", query_ollama(user_input))