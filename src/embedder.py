from sentence_transformers import SentenceTransformer

def embed_chunks(chunks, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    return model, embeddings
