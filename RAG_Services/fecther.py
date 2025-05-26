import numpy as np
from sentence_transformers import SentenceTransformer
from database.models import Document
from database.db import DBManager

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
        print('docuemnts:', len(docuemnts))
        for chunk in docuemnts:
            print("Comparing with chunk:", chunk.content[:50])
            similarity = cosine_similarity(query_embedding, chunk.embedding)
            results.append((chunk.content, similarity))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:topk]
if __name__ == "__main__":
    db_manager = DBManager()
    print("Configuring database engine...")
    top_chunks = search_db("Tcs's next year anunnual income projection:", topk=10, db_manager=db_manager)
    print("Top chunks found:")
    for i, (doc, score) in enumerate(top_chunks):
        print(f"\n🔹 Rank {i+1} (score: {score:.4f})\n{doc}")
