from src.config import PATHS , SEPARATORS, CHUNK_SIZE, CHUNK_OVERLAP, DIRECTORY , TOP_K , TOP_N, CHAT_MODEL, EMBEDDING_MODEL, WEIGHTS
from src.loader import load
from src.splitter import split
from src.vector import vectorize
from src.retriever import retrieve
from src.generator import build_chain , format_docs
from dotenv import load_dotenv

load_dotenv()
def pipe():
    docs = load(PATHS)
    chunks = split(docs, CHUNK_SIZE,CHUNK_OVERLAP, SEPARATORS)
    vector_store = vectorize(chunks, EMBEDDING_MODEL, DIRECTORY )
    retriever = retrieve(vector_store, WEIGHTS, TOP_K, chunks, TOP_N)
    return build_chain(CHAT_MODEL,retriever)
    


if __name__ == "__main__":
    chain = pipe()
    print(chain.invoke("what is the purpose of the eu act ? briefly."))