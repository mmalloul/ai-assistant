import os
import chromadb
import streamlit as st
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from src.config import DATA_DIRECTORY, DATABASE_PATH

def initialize_database() -> StorageContext:
    # Ensure the database path exists
    os.makedirs(DATABASE_PATH, exist_ok=True)

    try:
        with st.spinner("Initializing database... Please wait."):
            db = chromadb.PersistentClient(path=DATABASE_PATH)
            chroma_collection = db.get_or_create_collection("quickstart")
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            
        st.success("Database initialized successfully!")
    except Exception as e:
        st.error("Failed to initialize the database. Please check the system logs.")
        raise e

    return storage_context

def load_and_index_documents(storage_context: StorageContext = None) -> VectorStoreIndex | None:
    # Ensure the data directory exists
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    
    if not os.listdir(DATA_DIRECTORY):
        st.info("No documents found in the data directory.")
        return None

    with st.spinner("Indexing documents... Please wait."):
        documents = SimpleDirectoryReader(DATA_DIRECTORY, recursive=True).load_data()
        if documents:
            index = VectorStoreIndex.from_documents(documents, storage_context=storage_context if storage_context else StorageContext.from_defaults())
            st.success("Indexing complete!")
            return index
        
    return None
