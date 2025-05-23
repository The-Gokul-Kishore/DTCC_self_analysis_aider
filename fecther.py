import numpy as np
from sentence_transformers import SentenceTransformer
from models import Document
from db import DBManager

def cosine_similarity(v1:np.ndarray, v2:np.ndarray) -> float:
    """
    Calculate the cosine similarity between two vectors.
    Args:
        v1 (np.ndarray): First vector.
        v2 (np.ndarray): Second vector.
    Returns:
        float: Cosine similarity between the two vectors.
    """
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def search_db(query:str,topk:int,db_manager:DBManager) -> list:
    """
    Search the database for documents similar to the query.
    Args:
        query (str): The query string to search for.
        topk (int): The number of top similar documents to return.
        db_manager (DBManager): The database manager instance.
    Returns:
        list: A list of documents similar to the query.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([query])[0]

    with db_manager.session() as session:
        docuemnts = session.query(Document).all()
        
        results = []

        for chunk in docuemnts:
            similarity = cosine_similarity(query_embedding, chunk.embedding)
            results.append((chunk, similarity))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:topk]
if __name__ == "__main__":
    db_manager = DBManager()

    top_chunks = search_db("Explain the architecture of the system.", top_k=3, db_manager=db_manager)
    for i, (score, text) in enumerate(top_chunks):
        print(f"\n🔹 Rank {i+1} (score: {score:.4f})\n{text}")
