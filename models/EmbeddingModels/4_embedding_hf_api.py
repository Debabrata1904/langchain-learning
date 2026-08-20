import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN")
)

vector = client.feature_extraction(
    "Machine learning is a branch of artificial intelligence.",
    model="sentence-transformers/all-MiniLM-L6-v2"
)

print(vector[:10])
print(len(vector))