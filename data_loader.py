import os

from grpc._cython.cygrpc import SendMessageOperation
from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
reader = PDFReader()
EMBED_MODEL = 'text-embedding-3-large'
EMBED_DIM = 3072

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_data_chunk_pdf(path: str):
    docs = PDFReader(path:str)
    texts = [d.text for d in docs if getattr(d, 'text', None)]
    chunks = []

    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_text(text: list[str]) -> list[[str[float]]):
    responses = client.embeddings.create(model=EMBED_MODEL, input = texts,)
    return [item.embedding for item in response.data]
