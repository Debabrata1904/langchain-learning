from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

documents = [
    "Machine learning is a branch of artificial intelligence.",
    "Deep learning is a subset of machine learning.",
    "Python is a popular programming language.",
    "The weather is very hot today."
]

query = "What is machine learning?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity between the query and each document
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find the index of the most similar document
most_similar_index = similarities.argmax()

print("Query:", query)
# Print the most similar document
print(documents[most_similar_index])
print("Similarity score:", similarities[most_similar_index])