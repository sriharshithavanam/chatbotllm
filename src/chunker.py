def chunk_text(text, max_length=500):
    sentences = text.split('\n')
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_length:
            chunk += sentence + "\n"
        else:
            chunks.append(chunk.strip())
            chunk = sentence + "\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks
