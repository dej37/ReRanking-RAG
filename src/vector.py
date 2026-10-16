import os
from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings

def vectorize(chunks, embedding_model, directory):
    embeddings = MistralAIEmbeddings(model=embedding_model)
    if os.path.exists(directory):
        return Chroma(
            collection_name="ai_law",
            embedding_function=embeddings,
            persist_directory=directory,
        )
    return Chroma.from_documents(
        chunks,
        embeddings,
        collection_name="ai_law",
        persist_directory=directory,
    )