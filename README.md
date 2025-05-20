# 🚀 Revolutionizing Enterprise Data with AWS Bedrock, PDFs, VectorDB, and RAG

Unstructured data is everywhere—locked inside PDFs, JSON files, and other document formats. But how can enterprises transform this data into actionable insights?

This project presents a **dual-platform, end-to-end solution** built on AWS, enabling enterprises to unlock and query unstructured content using state-of-the-art AI and Vector Databases.

---

## 💡 Key Components

### 1. **Client Application**
A user-friendly interface where users can ask natural language questions about their documents.

- Powered by **LLMs from AWS Bedrock**, such as **Anthropic Claude** and **Titan Embeddings**
- Seamless document understanding and question answering (Q&A)
- Real-time responses using **Retrieval-Augmented Generation (RAG)**

### 2. **Admin Portal**
A powerful backend interface for data ingestion and vector indexing.

- Upload **PDFs** and **JSON files**
- Automatically extract and preprocess content
- Split content into manageable chunks
- Generate and store **vector embeddings** using **FAISS** in **S3 buckets**

---

## 🔍 Why This Is a Game-Changer

✅ **Serverless AI via AWS Bedrock**: Harness the power of cutting-edge LLMs without managing infrastructure  
✅ **Robust Document Processing**: No data left behind—scanned or native documents supported  
✅ **VectorDB in S3**: High-performance semantic search over huge datasets  
✅ **RAG-powered Accuracy**: Context-rich retrieval combined with generation ensures relevant, reliable outputs  
✅ **Fully Dockerized**: Both portals are containerized and deployed on AWS EC2 for scalability and ease of maintenance  

---

## 🛠️ Technologies Used

- **AWS Bedrock** (LLMs & embeddings)
- **FAISS** (Vector DB)
- **LangChain** (Text splitting & embeddings integration)
- **PyMuPDF / fitz** (PDF processing)
- **OpenAI GPT-4 Vision** (OCR fallback)
- **Docker** (Containerized deployment)
- **EC2 + S3** (Hosting & storage)

---

## 📦 Architecture Overview

```

PDF / JSON Files ───▶ Admin Portal ───▶ Chunking & Embedding ───▶ VectorDB (FAISS on S3)
│
▼
Hosted LLMs via AWS Bedrock
│
▼
Client Portal ◀── RAG-based Question Answering

```

---

## 🧪 Example Use Cases

- Legal document Q&A
- Research paper summarization
- Enterprise data lake mining
- Internal knowledge base search

---

## 🚢 Deployment

Both portals are:

- ✅ Dockerized and published to DockerHub
- ✅ Hosted on EC2 instances
- ✅ Designed for scalability and security

---

## 📷 Screenshot

![Enterprise Data Pipeline Screenshot](https://github.com/user-attachments/assets/3ef7d933-88cc-458d-9d2f-768c3466447e)

---


