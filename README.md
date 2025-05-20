**Revolutionizing Enterprise Data with AWS Bedrock, PDFs, VectorDB, and RAG
**

Data is everywhere—hidden in PDFs, JSON files, and other documents. But how do you make sense of it all? Enter AWS Bedrock, VectorDB stored in S3, and the Retrieval-Augmented Generation (RAG) approach! 

Recently, we built a robust dual-platform solution:
1) **Client Application**: A user-friendly interface where you can ask questions about your data, powered by cutting-edge LLMs like Anthropic Claude and Titan Embeddings. This platform makes document understanding and Q&A seamless.

2) **Admin Portal**: A dynamic tool to preprocess data. Upload PDFs or JSON files, extract their content, split them into manageable chunks, and create FAISS-based VectorDBs stored in S3 buckets.

Here’s what makes this solution a game-changer:
  1. AWS Bedrock drives high-performance, serverless AI capabilities.
  2. PDF and JSON processing ensures every byte of information is usable.
  3. VectorDB enables fast, semantic search over vast document repositories.
  4. RAG (Retrieval-Augmented Generation) connects context-rich retrieval with generative AI for precise, context-aware responses.

Each Admin and Client portals are dockerized, pushed to dockerhub and hosted over EC2 instance.
With this solution, businesses can transform unstructured data into actionable insights, empowering smarter decision-making across industries.


![image](https://github.com/user-attachments/assets/3ef7d933-88cc-458d-9d2f-768c3466447e)
