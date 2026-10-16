from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pathlib import Path

def format_docs(docs):
    return "\n\n".join(
        f"[{Path(d.metadata['source']).name}, p.{d.metadata['page'] + 1}]\n{d.page_content}"
        for d in docs
    ) 

prompt = """ answer the question using only the context below.
    After each claim, cite its source in brackets, exactly as labelled in the context.
    If the context does not contain the answer, say you don't know.
    Context: 
    
    {context}
    Question:
    {question}

    Answer:"""


def build_chain(model,retriever):
    prompt_template = PromptTemplate.from_template(prompt)
    llm = ChatMistralAI(model=model, temperature = 0)

    chain =(
        {"context": retriever | format_docs , "question" : RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )
    return chain