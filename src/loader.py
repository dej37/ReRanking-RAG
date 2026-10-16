from langchain_community.document_loaders import PyPDFLoader
def load(paths):
    docs=[]
    for path in paths:
        loader=PyPDFLoader(path)
        docs.extend(loader.load())
        return docs

   