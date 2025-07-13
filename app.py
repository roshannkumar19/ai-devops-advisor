import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get keys from .env
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

# Create client (NEW METHOD)
client = OpenAI(
    api_key=api_key,
    base_url=api_base
)

# Function to ask AI
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

# Streamlit UI
st.set_page_config(page_title="DevOps AI Assistant", page_icon="🤖")
st.title("🧠 DevOps AI Assistant")
st.write("Ask me anything about AWS, Docker, Terraform, CI/CD...")

# Text input
user_input = st.text_input("Your Question:")

# Handle response
if user_input:
    with st.spinner("Thinking..."):
        try:
            answer = ask_agent(user_input)
            st.success("AI Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
