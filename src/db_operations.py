import os
import chromadb
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from src.config import DATA_DIRECTORY

def initialize_database():
    with st.spinner("Initializing database... Please wait."):
        db = chromadb.PersistentClient(path="./chroma_db")
        chroma_collection = db.get_or_create_collection("quickstart")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
    st.info("Database initialized!")
    return storage_context

def load_and_index_documents(storage_context):
    if os.path.exists(DATA_DIRECTORY) and os.listdir(DATA_DIRECTORY):
        with st.spinner("Indexing documents... Please wait."):
            documents = SimpleDirectoryReader(DATA_DIRECTORY, recursive=True).load_data()
            index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
        st.info("Indexing complete!")
        return index
    else:
        return None
