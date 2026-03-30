from openai import OpenAI
from dotenv import load_dotenv
import os
import pymupdf
from pathlib import Path
import numpy as np
from db import get_db_connection

load_dotenv()

INFERENCE_ENDPOINT = os.getenv("INFERENCE_ENDPOINT")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
API_KEY = os.getenv("GITHUB_API_KEY")

client = OpenAI(base_url=INFERENCE_ENDPOINT, api_key=API_KEY)

def get_similar_chunks(query: str, num_of_relevant_chunks=3):
    conn = get_db_connection()
    query_embedding = _embed_query(query)
    embedded_query = np.array(query_embedding, dtype=np.float32)

    rows = conn.execute(
        "SELECT chunk FROM rag_index WHERE embedding MATCH ? LIMIT ?",
        (embedded_query, num_of_relevant_chunks)
    ).fetchall()

    return [row[0] for row in rows]


def embed_documents():
    pdf_text = _pdf_to_text("documents/Afakass_LLC_Code_of_Conduct.pdf")
    chunked_text = _simple_test_splitter(pdf_text)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS rag_index USING vec0(
        chunk TEXT,
        embedding FLOAT[3072]
    );
    """)

    embeddings = _get_embeddings(chunks=chunked_text)

    for chunk, embedding_array in zip(chunked_text, embeddings):
        cursor.execute(
            "INSERT INTO rag_index (chunk, embedding) VALUES (?, ?)",
            (chunk, embedding_array)
        )

    conn.commit()
    conn.close()

def _get_embeddings(chunks: list[str]) -> list[float]:
    response = client.embeddings.create(
        input=chunks,
        model=EMBEDDING_MODEL
    )

    return [np.array(e.embedding, dtype=np.float32) for e in response.data]

def _embed_query(query: str):
    response = client.embeddings.create(
        input=query,
        model=EMBEDDING_MODEL
    )
    
    return response.data[0].embedding


def _simple_test_splitter(text: str, chunk_size: int =200, overlap: int = 30) -> list[str]:
    chunks = []

    for i in range(0, len(text), chunk_size):
        if i == 0:
            chunks.append(text[i-0:i+chunk_size])
            continue
        chunks.append(text[i-overlap:i+chunk_size])
    
    return chunks

def _pdf_to_text(file_path: Path) -> str:
    text = ""
    document = pymupdf.open(file_path)

    for page in document:
        text += page.get_text()
    
    return text
