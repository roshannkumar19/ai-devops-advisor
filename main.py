import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def ask_agent(question):
    system_prompt = (
        "You are a professional DevOps assistant. "
        "Answer in detail with code examples for AWS, Docker, CI/CD, and Terraform."
    )
    response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    print("🔧 DevOps AI Agent Ready! Type your question (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = ask_agent(user_input)
        print(f"\n🤖 AI: {reply}\n")
