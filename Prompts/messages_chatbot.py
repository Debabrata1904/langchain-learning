from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
        
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content[0]["text"]))
    print("AI:", response.content[0]["text"])

print("\nChat History:")
for message in chat_history:
    print(f"{type(message).__name__}: {message.content}")