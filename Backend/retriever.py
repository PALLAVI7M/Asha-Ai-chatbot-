import json
import cohere

# Load knowledge base
with open('backend/data/knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

def cosine_similarity(vec1, vec2):
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    norm1 = sum(a*a for a in vec1) ** 0.5
    norm2 = sum(b*b for b in vec2) ** 0.5
    return dot_product / (norm1 * norm2)

def retrieve_answer(query, co):
    documents = [item['content'] for item in knowledge_base]
    
    # Embed documents
    docs_embeddings = co.embed(texts=documents, model='embed-english-v3.0').embeddings
    
    # Embed query
    query_embedding = co.embed(texts=[query], model='embed-english-v3.0').embeddings[0]
    
    similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in docs_embeddings]
    
    # Find best match
    best_match_idx = similarities.index(max(similarities))
    best_document = documents[best_match_idx]
    
    # Generate answer
    prompt = f"""
You are Asha, an AI chatbot designed to assist users with information about women careers, job opportunities, mentorship programs, and events.

User Query: {query}
Relevant Info: {best_document}

Answer the user concisely, ethically, and encouragingly.
"""
    
    response = co.generate(
        prompt=prompt,
        model='command-r-plus',
        temperature=0.4,
        max_tokens=200
    ).generations[0].text.strip()
    
    return response
  
