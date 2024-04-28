import os
from config.config import DATA_DIRECTORY, DATABASE_PATH
import chromadb
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore

def initialize_database() -> StorageContext:
    os.makedirs(DATABASE_PATH, exist_ok=True)
    try:
        db = chromadb.PersistentClient(path=DATABASE_PATH)
        chroma_collection = db.get_or_create_collection("quickstart")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        print(f"Database initialized at {DATABASE_PATH}")
        return storage_context
    except Exception as e:
        print(f"Failed to initialize database: {str(e)}")
        return None

def load_and_index_documents(storage_context: StorageContext) -> VectorStoreIndex | None:
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    
    try:
        documents = SimpleDirectoryReader(DATA_DIRECTORY, recursive=True).load_data()
        index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
        print("Documents indexed successfully.")
        return index
    except Exception as e:
        print(f"Failed to load and index documents: {str(e)}")
        return None
