from langchain_text_splitters import RecursiveCharacterTextSplitter

def split(docs, chunk_size, chunk_overlap,separators):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, 
                                              chunk_overlap=chunk_overlap,
                                              separators=separators)
    chunks = splitter.split_documents(docs)
    return chunks