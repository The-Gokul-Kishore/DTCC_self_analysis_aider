import fitz  
from sentence_transformers import SentenceTransformer
#import faiss
import numpy as np
from database.db import DBManager
from database.models import Document
print("Loading PDF...")
def load_pdf(load_path: str, chunk_size: int = 500) -> list:
    """
    Extract text from PDF and chunk it into smaller pieces.
    Args:
        load_path (str): The path to the PDF file.
        chunk_size (int): Number of characters per chunk.
    Returns:
        list: A list of text chunks.
    """
    print("Extracting text from PDF using fitz (PyMuPDF)...")
    doc = fitz.open(load_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    # Simple character-based chunking
    chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks

def parser(load_path: str,chunk_size:int = 500) -> list:
    """
    Parse a PDF file and return its content as a list of strings.
    Args:
        load_path (str): The path to the PDF file to be parsed.
    
    """
    print("Loading PDF...")
    chunks = load_pdf(load_path,chunk_size=chunk_size)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Encoding PDF...")
    embeddings = model.encode(chunks,show_progress_bar=True)
    print("Normalizing embeddings...")
    embeddings = embeddings/np.linalg.norm(embeddings, axis=1, keepdims=True)
    # print("Creating FAISS index...")
    # dimension = embeddings.shape[1]
    # index = faiss.IndexFlatIP(dimension)
    # print("Adding embeddings to FAISS index...")
    # index.add(np.array(embeddings))
    save_to_db(chunks,embeddings,db_manager=DBManager())
def save_to_db(chunks,embeddings,db_manager: DBManager) -> None:
    with db_manager.session() as session:
        cnt = 0
        for chunk, embedding in zip(chunks, embeddings):
            cnt += 1
            print("Saving chunk to database...")
            doc = Document(
                content=chunk,
                embedding=embedding.tolist()
            )
            session.add(doc)
        print(f"Total {cnt} chunks saved to database.")
        print("Committing session to database...")
        session.commit()

if __name__ == "__main__":
    print("Starting PDF parser...")
    parser("C:/Users/GOKUL/Downloads/annual-report-2023-2024.pdf", chunk_size=1000)
