# 📊 InsightLedgerAI — RAG-Powered Financial Document Summarizer

**InsightLedgerAI** is a lightweight **RAG (Retrieval-Augmented Generation)** application built using **Ollama 3.1B Instruct**. It allows users to upload financial documents (like balance sheets, ledgers, reports), and it returns relevant **summaries**, **key insights**, and **basic calculations** — all in real-time.

🎯 Ideal for **students** and **learners** who want to understand financial data without diving deep into jargon or spreadsheets.

---

## 🧠 How It Works

1. 📝 Upload your **financial document** (PDF, TXT, or structured formats)
2. 📚 The content is **embedded using MiniLM-3** and stored in a **FAISS** vector DB
3. 🧠 Ollama 3.1B Instruct is used to **generate smart, concise summaries**
4. 📈 Outputs include totals, observations, and simplified calculations

---

## 🚀 Tech Stack

| Tech          | Description                                 |
|---------------|---------------------------------------------|
| **Flask**     | Lightweight Python web framework            |
| **HTML/CSS/JS** | Simple and responsive frontend             |
| **LangChain (Community)** | Framework for chaining LLM logic |
| **Ollama 3.1B Instruct** | Local LLM used for generation      |
| **FAISS (CPU)** | Vector store for fast similarity search   |
| **MiniLM-3**  | Embedding model used for semantic matching  |

---

## 📦 Setup & Installation

### 🔧 Requirements
- Python 3.10+
- Ollama installed locally
- FAISS CPU version
- Flask

### 🛠️ Install Dependencies

```bash
git clone https://github.com/your-username/insightledgerai.git
cd insightledgerai
pip install -r requirements.txt
```
## ✨ Features
📄 Upload financial documents

🧠 Get key summaries and explanations

📊 Simple calculations and metric extractions

⚡ Fast local inference with Ollama

🔍 Intelligent context matching with FAISS

## 📌 Use Cases
🏫 Financial accounting students

📚 Quick summarization before exams

📈 Audit prep and report understanding

🧾 Simplifying income/expense breakdowns

## 🙋‍♂️ Author
Made by Siddharth, Vikram, Akul with 💡 for learners who hate scrolling through Excel sheets.

Feedback, suggestions, and contributions are always welcome!