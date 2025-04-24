import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from config import INDEX_PATH, CHUNKS_PATH
from src.llm_deepseek import DeepSeekLLM

def get_qa_chain():
    # Load FAISS index
    index = faiss.read_index(INDEX_PATH)

    # Load chunks
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    # Load embedding model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    llm = DeepSeekLLM()

    def query_handler(query):
        query_vec = model.encode([query])
        D, I = index.search(np.array(query_vec), k=3)
        retrieved_chunks = [chunks[i] for i in I[0]]
        context = "\n".join(retrieved_chunks)
        prompt = f"Context:\n{context}\n\nQuestion:\n{query}"
        return llm(prompt)

    return query_handler
