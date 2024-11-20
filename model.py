import chromadb
import logging
import sys

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import (
    Settings, VectorStoreIndex, SimpleDirectoryReader, PromptTemplate)
from llama_index.core import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def init_llm():
    llm = Ollama(model="phi3", request_timeout=300.0)
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.llm = llm
    Settings.embed_model = embed_model


def init_index(embed_model):
    reader = SimpleDirectoryReader("./docs")
    documents = reader.load_data()

    logging.info("index creating with `%d` documents", len(documents))

    chroma_client = chromadb.EphemeralClient()
    chroma_collection = chroma_client.create_collection("iollama")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # use this to set custom chunk size and splitting
    # https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/

    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model)

    return index


def init_query_engine(index):
    template = """
                You are a knowledgeable assistant for Sidekick, an AI-powered automation and cross-listing platform for online resellers. Use the loaded text to provide accurate, concise, and user-friendly answers about Sidekick’s features, benefits, troubleshooting, and usage tips. Maintain a professional tone, structure responses clearly, and focus on enhancing user productivity. Redirect users to relevant parts of the loaded content where appropriate.

                Here is some context related to the query: {context_str}
                
                Considering the above information, please respond to the following customer inquiry with detailed references to PoshSideKick's offerings, or company values where appropriate:

                **Note:** If the inquiry includes greetings or casual conversation, acknowledge them briefly and then focus on providing a precise and relevant answer to the main question.
                
                User Input: {query_str}"""

    qa_template = PromptTemplate(template)

    query_engine = index.as_query_engine(
        text_qa_template=qa_template, similarity_top_k=3)

    return query_engine


def chat(query_engine,input_question, user=None):
    response = query_engine.query(input_question)
    logging.info("got response from llm - %s", response)
    return response.response


def chat_cmd(query_engine):
    while True:
        input_question = input("Enter your question (or 'exit' to quit): ")
        if input_question.lower() == 'exit':
            break

        response = query_engine.query(input_question)
        logging.info("got response from llm - %s", response)


if __name__ == '__main__':
    init_llm()
    index = init_index(Settings.embed_model)
    query_engine = init_query_engine(index)
    chat_cmd(query_engine)
