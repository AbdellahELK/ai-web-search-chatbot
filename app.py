
import streamlit as st
import os
import requests

from dotenv import load_dotenv
from openai import OpenAI

# ==========================================
# 1. CONFIGURATION
# ==========================================

load_dotenv()

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# ==========================================
# 2. WEB SEARCH FUNCTION
# ==========================================

def search_web(query):

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 5
    }

    response = requests.post(
        url,
        json=payload,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    results = []

    for result in data.get("results", []):
        results.append(
            f"""
            Title: {result.get('title', '')}
            URL: {result.get('url', '')}
            Content: {result.get('content', '')}
            """
        )

    return "\n".join(results)


# ==========================================
# 3. CHATBOT INTERFACE
# ==========================================

st.title("🤖 My AI Chatbot")

st.caption("AI assistant powered by Groq + Web Search")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Settings")

    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("**Model:** GPT-OSS 120B")
    st.write("**Search:** Tavily")


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==========================================
# 4. USER INPUT
# ==========================================

prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # ==========================================
    # 5. AI RESPONSE
    # ==========================================

    with st.chat_message("assistant"):

        with st.spinner("Searching the web and thinking..."):

            try:

                # Search the web
                web_results = search_web(prompt)

                # System instructions
                system_message = f"""
                You are a helpful AI assistant.

                You have access to web search results.

                Instructions:
                - Answer clearly and naturally.
                - Use the web search results when relevant.
                - Prefer recent information for questions about current events.
                - Never invent facts.
                - If the results do not contain the answer, say so.
                - Include relevant source URLs at the end of your answer.
                - You can use your own knowledge for general questions.

                WEB SEARCH RESULTS:
                {web_results}
                """

                # Build conversation
                messages = [
                    {
                        "role": "system",
                        "content": system_message
                    }
                ]

                # Add conversation history
                messages.extend(st.session_state.messages)

                # Call Groq
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages,
                    temperature=0.3
                )

                answer = response.choices[0].message.content

                # Display answer
                st.markdown(answer)

                # Save answer
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.exceptions.RequestException as e:

                st.error(f"Web search error: {e}")

            except Exception as e:

                st.error(f"AI error: {e}")
