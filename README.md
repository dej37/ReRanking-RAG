# AI Law Assistant

A question-answering app over three AI governance documents. Ask a question in plain language and get an answer with citations to the exact file and page it came from.

**Documents indexed**

| File | Document |
|---|---|
| `eu_act.pdf` | EU AI Act, Regulation (EU) 2024/1689 (original 2024 text) |
| `gdpr.pdf` | GDPR, Regulation (EU) 2016/679 |
| `ai_risk.pdf` | NIST AI Risk Management Framework 1.0 (NIST AI 100-1) |

> The EU AI Act was amended in 2026. This project answers from the original 2024 text, not the amended version.

## How it works

```
question
   |
   v
vector search (Chroma + Mistral embeddings) --+
                                              +--> merged candidates --> reranker --> top chunks --> LLM --> cited answer
keyword search (BM25) ------------------------+
```

1. **Load and split.** PDFs are loaded page by page and split into chunks of about 1500 characters. The splitter prefers to cut at "Article" headings before cutting anywhere else.
2. **Hybrid retrieval.** Vector search finds chunks with a similar meaning. BM25 finds chunks with the same words. The two ranked lists are merged.
3. **Reranking.** A cross-encoder (`BAAI/bge-reranker-base`) reads the question together with each candidate and keeps the best few.
4. **Generation with citations.** Each chunk is labelled `[file, p.N]` in the prompt, and the model (`open-mistral-nemo`) is told to answer only from the context and cite those labels.
5. **Streamlit UI** for asking questions.

## Setup

Requires Python 3.13 (Python 3.14 caused install problems with some ML packages).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
MISTRAL_API_KEY=your_key_here
```

Put the three PDFs in the `data/` folder, then run:

```bash
streamlit run app.py
```

The first start builds the vector index (slow, uses API calls). Later starts reuse the saved `chroma_db/` folder. **If you change the documents or the chunking settings, delete `chroma_db/` once so the index is rebuilt.**

## Project structure

```
app.py            Streamlit app
src/
  config.py       settings (paths, chunk size, models, top-k)
  loader.py       PDF loading
  splitter.py     chunking
  vector.py       Chroma index (build once, then reuse)
  generator.py    prompt and answer chain
  pipeline.py     wires everything together
```

## Evaluation

_Not done yet._ Planned: a set of 15-20 questions with known correct answers (for example, which article answers each question), measuring how often the right chunk is retrieved with each setup.

| Setup | Right chunk in top 5 |
|---|---|
| Vector search only | TBD |
| + BM25 (hybrid) | TBD |
| + reranking | TBD |
| + article-aware chunking | TBD |

## Known limitations

- **Incomplete answers on list-style questions.** Asking "What practices are prohibited under the EU AI Act?" returns only some of the practices in Article 5. Many results are recitals (the explanatory preamble), which use similar wording to the binding article, and the opening of Article 5 often does not reach the model. This question is kept as a baseline to measure improvements against.
- **Wrong labels in answers.** The model sometimes gives a heading that does not match the cited text. The citation points to the right page, but the answer should be checked against the source.
- **Not legal advice.** This is a learning project. Always check the original text.

## Roadmap

- [ ] Evaluation set and results table
- [ ] Chat history, so follow-up questions work
- [ ] Better chunking for legal articles
- [ ] Deployment