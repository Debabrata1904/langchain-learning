from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    timeout=30,
    max_retries=0
)

print("Model ID:", model.model)
print("Testing...", flush=True)

try:
    response = model.invoke("Reply with only: Hello")
    print("Success:", response.content)
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Error details:", str(e))