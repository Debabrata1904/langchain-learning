from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    #max_output_tokens=200
)

messages = [
    SystemMessage(
        content="You are a helpful AI teacher. Give short anshwers."
        ),
    HumanMessage(
        content="What is machine learning?"
    )
]

result = chat_model.invoke(messages)

print(result.content[0]["text"])