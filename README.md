# AI Web Search Chatbot

An AI-powered chatbot that combines Large Language Models (LLMs) with web search capabilities to provide conversational and up-to-date answers.

Built with Python, Streamlit, Groq API, and Tavily Search API.

## Overview

Traditional LLM-based chatbots rely mainly on their training knowledge, which may not include recent events or updated information.

This project addresses this limitation by integrating a web search API into the chatbot workflow. It retrieves relevant online information and provides it as context to the LLM before generating a response.

## Features

- **AI-powered conversations:** Generate natural language responses using GPT-OSS 120B through Groq.
- **Web search integration:** Retrieve recent online information using Tavily Search API.
- **Context-aware conversations:** Maintain conversation history during the active session.
- **Source references:** Display relevant search results and source URLs.
- **Interactive interface:** Chat interface developed with Streamlit.
- **Environment-based configuration:** Securely manage API keys using environment variables.

## Architecture

```text
             User
               |
               v
        Streamlit Interface
               |
               v
        Python Application
               |
          Tavily API
               |
         Web Search Results
               |
               v
           Groq API
          GPT-OSS 120B
               |
               v
        Generated Response
               |
               v
             User
```

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Chat interface |
| Groq API | LLM inference |
| GPT-OSS 120B | Language model |
| Tavily API | Web search |
| Requests | HTTP communication |
| python-dotenv | Environment configuration |

## Project Structure

```text
ai-web-search-chatbot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-web-search-chatbot.git

cd ai-web-search-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your API keys:

- Groq: https://console.groq.com/
- Tavily: https://app.tavily.com/

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL provided by Streamlit.

## How It Works

1. The user submits a question through the Streamlit interface.
2. The application sends a search request to Tavily.
3. Relevant search results are retrieved and formatted.
4. Search results and conversation history are provided as context to the LLM.
5. Groq generates a natural language response.
6. The application displays the answer and its associated sources.

## Future Improvements

- Intelligent search decisions using LLM tool calling.
- Persistent conversation history with SQLite.
- Streaming AI responses.
- Improved source relevance and citation handling.
- Document-based question answering using RAG.
- Conversation management and multiple chat sessions.

## Author

Developed as a practical project to explore Generative AI, Large Language Models, API integration, and AI Engineering.

## License

MIT License
