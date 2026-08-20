from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-100")

texts = [
    "Machine learning is useful.",
    "I am learning artificial intelligence.",
    "Today the weather is hot."
]

vectors = embeddings.embed_documents(texts)

print(len(vectors))