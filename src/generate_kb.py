import os
import faiss
import pickle
from src.pdf_reader import extract_text_from_pdf
from src.chunker import chunk_text
from src.embedder import embed_chunks
from src.retriever import build_faiss_index

from config import INDEX_PATH, CHUNKS_PATH

# Load and chunk text
pdf_path = "Data/data.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(text)

# Embeddings
model, embeddings = embed_chunks(chunks)

# FAISS Index
index = build_faiss_index(embeddings)

# Save index & chunks
faiss.write_index(index, INDEX_PATH)
with open(CHUNKS_PATH, "wb") as f:
    pickle.dump(chunks, f)

print("✅ Knowledge base generated successfully!")
