from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []

while True:

    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("⏳ Sending request...")

    prompt = chat_prompt.invoke({
        "chat_history": chat_history,
        "query": user_input
    })

    print("✅ Prompt created")
    print("⏳ Calling Gemini...")

    response = model.invoke(prompt)

    print("✅ Gemini responded")

    ai_message = response.content[0]["text"]

    print("AI:", ai_message)

    chat_history.append(
        HumanMessage(content=user_input)
    )

    chat_history.append(
        AIMessage(content=ai_message)
    )