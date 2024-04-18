import os
import chromadb
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from src.config import DATA_DIRECTORY, DATABASE_PATH

def initialize_database() -> StorageContext:
    os.makedirs(DATABASE_PATH, exist_ok=True)

    try:
        db = chromadb.PersistentClient(path=DATABASE_PATH)
        chroma_collection = db.get_or_create_collection("quickstart")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
    except Exception as e:
        return None

    return storage_context

def load_and_index_documents(storage_context: StorageContext = None) -> VectorStoreIndex | None:
    os.makedirs(DATA_DIRECTORY, exist_ok=True)
    
    if not os.listdir(DATA_DIRECTORY):
        return None

    documents = SimpleDirectoryReader(DATA_DIRECTORY, recursive=True).load_data()
    
    if documents:
        if storage_context:
            index: VectorStoreIndex = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

            return index
        else:
            index: VectorStoreIndex = VectorStoreIndex.from_documents(documents)

            return index
    return None
