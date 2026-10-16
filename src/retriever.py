from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
def retrieve(vector_store , weights, k, chunks, top_n):
    preretriever = vector_store.as_retriever(search_type = "similarity", search_kwargs = {"k": k})
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = k

    hybrid = EnsembleRetriever(
        retrievers = [preretriever , bm25],
        weights = weights
    )

    cross_encoder = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")
    reranker = CrossEncoderReranker(model = cross_encoder, top_n = top_n)

    retriever = ContextualCompressionRetriever(
        base_compressor = reranker,
        base_retriever = hybrid
    )

    return retriever