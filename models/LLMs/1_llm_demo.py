from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3.6-flash"
)

result = llm.invoke("What is the capital of India?")

print(result)