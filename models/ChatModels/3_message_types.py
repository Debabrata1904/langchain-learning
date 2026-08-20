from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    max_output_tokens=200
)

messages = [
    SystemMessage(
        content="You are a helpful AI teacher. Give short answers."
    ),

    HumanMessage(
        content="What is machine learning?"
    ),

    AIMessage(
        content="Machine learning is a way for computers to learn patterns from data."
    ),

    HumanMessage(
        content="Give me one real-world example."
    )
]

result = chat_model.invoke(messages)

print(result.content)