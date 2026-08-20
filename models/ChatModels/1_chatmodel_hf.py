from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=200,
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("Explain machine learning in simple language.")

print(result.content)