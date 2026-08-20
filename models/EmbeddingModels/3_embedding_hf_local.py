from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_HOME"] = "D:/huggingface"
os.environ["HF_HUB_CACHE"] = "D:/huggingface/hub"


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embeddings.embed_query(
    "Machine learning is a branch of artificial intelligence."
)

'''
texts = [
    "Machine learning is useful.",
    "I am learning artificial intelligence.",
    "Today the weather is hot."
]

vector = embeddings.embed_documents(texts)
'''
print(vector)
print(len(vector))