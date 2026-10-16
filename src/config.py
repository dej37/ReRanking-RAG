PATHS =[r'C:\Users\Top Prix\OneDrive\New folder\ReRank_RAG\data\ai_risk.pdf',
r'C:\Users\Top Prix\OneDrive\New folder\ReRank_RAG\data\eu_act.pdf',
r'C:\Users\Top Prix\OneDrive\New folder\ReRank_RAG\data\gdpr.pdf']

CHUNK_SIZE = 1800
CHUNK_OVERLAP = 300
DIRECTORY = 'chroma_db'
TOP_K=20
CHAT_MODEL='open-mistral-nemo'
EMBEDDING_MODEL = 'mistral-embed'
WEIGHTS=[0.8,0.2]
TOP_N = 15
SEPARATORS= [
    "\nCHAPTER ",
    "\nChapter ",
    "\nSECTION ",
    "\nSection ",
    "\nArticle ",
    "\nARTICLE ",
    "\n\n",
    "\n",
    ". ",
    " ",
    "",
]