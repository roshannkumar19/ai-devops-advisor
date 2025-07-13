import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

# Function to handle question-answering
def ask_agent(question):
    system_prompt = (
        "You are a professional DevOps assistant. "
        "Answer in detail with code examples for AWS, Docker, CI/CD, and Terraform."
    )

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

# CLI interaction
if __name__ == "__main__":
    print("🤖 DevOps AI Agent (CLI) - type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        try:
            reply = ask_agent(user_input)
            print(f"\nAI: {reply}\n")
        except Exception as e:
            print(f"\nError: {e}\n")
