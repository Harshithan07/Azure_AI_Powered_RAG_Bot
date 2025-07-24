# FoundryRAG: Azure AI-Powered Document QA Bot

---

## 🔍 Project Overview

Every organization has valuable knowledge locked away in PDFs, manuals, and internal documentation. FoundryRAG unlocks that content through a modular, production-leaning **Retrieval-Augmented Generation (RAG)** system powered by **Azure AI Foundry**.

This project converts raw documents into searchable, intelligent knowledge bases. It enables users to ask natural language questions and receive grounded, LLM-powered responses—just like ChatGPT, but trained on your documents.

---

### 🧠 The pipeline includes:

* Chunked parsing of `.pdf` and `.txt` documents
* Embedding generation using Hugging Face sentence transformers
* FAISS vector store indexing and retrieval
* Azure OpenAI integration via LangChain for grounded answer generation
* Environment-isolated Python modules for ingestion, search, and generation
* CLI and app-based chatbot interface

Built entirely from scratch, this project was my attempt to deeply understand the architecture behind RAG systems—and to demonstrate how an enterprise-ready document assistant can be designed without relying on third-party wrappers or black-box tools.

---

## 📁 Key Modules

| File                    | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| `document_processor.py` | Parses and splits documents into overlapping chunks         |
| `embedding_indexer.py`  | Generates vector embeddings and builds FAISS index          |
| `rag_chain.py`          | Core RAG logic combining retrieval and generation           |
| `chatbot.py`            | CLI chatbot interface for asking questions                  |
| `ragapp.py`             | App entry point (can be adapted into a web or Streamlit UI) |
| `.env`                  | API keys for HuggingFace and Azure OpenAI                   |
| `requirements.txt`      | Python dependency list                                      |

---

## 🧱 Setup and Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/foundryrag.git
cd foundryrag

# Set up virtual environment
python3 -m venv msbaenv
source msbaenv/bin/activate  # On Windows: msbaenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Install **ffmpeg** if you're planning to expand the project to audio RAG:

```bash
# Mac
brew install ffmpeg

# Ubuntu
sudo apt-get install ffmpeg
```

Set up environment variables:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token
OPENAI_API_KEY=your_azure_openai_key
```

---

## 🚀 How to Run

### Step 1: Index Your Documents

```bash
python embedding_indexer.py
```

This will:

* Parse and chunk `.pdf`/`.txt` files
* Generate and store vector embeddings using Hugging Face models
* Create or update a local FAISS index

### Step 2: Start the Chatbot

```bash
python chatbot.py
```

Ask queries like:

```
"What are the key steps in Azure AI Foundry's RAG pipeline?"
"Summarize the use cases supported in the uploaded documents."
```

---

## 📊 What You’ll See

* Token-aware chunking of documents
* Top-k retrieval from FAISS with cosine similarity
* Context-aware responses using Azure-hosted GPT
* CLI interaction for rapid experimentation
* Modular code ready to integrate into dashboards, APIs, or agentic tools

---

## 💡 Use Cases

* Internal enterprise search
* Legal/contract document assistants
* Support agent knowledge copilots
* Academic paper Q\&A
* Technical manual summarizers

---

## 🧪 Future Enhancements

* Add multi-document support and metadata filtering
* Deploy a Streamlit dashboard for user-friendly access
* Integrate MLflow to track query relevance and feedback
* Replace CLI with a LangChain Agent for tool-based reasoning
* Extend to multimodal inputs (e.g., add Whisper for audio transcription)

---
