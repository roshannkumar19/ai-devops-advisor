import os
import openai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
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

# Streamlit Web UI
st.set_page_config(page_title="DevOps AI Assistant", page_icon="🧠")
st.title("🤖 DevOps AI Assistant")
st.write("Ask me anything about AWS, Docker, CI/CD, Terraform, etc.")

user_input = st.text_input("💬 Ask a DevOps question:")
if user_input:
    with st.spinner("Thinking..."):
        answer = ask_agent(user_input)
        st.markdown(f"**🧠 AI:** {answer}")
