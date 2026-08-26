from langchain_core.load import loads
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Load the prompt from the JSON file
with open("my_prompt.json", "r", encoding="utf-8") as f:
    json_data = f.read()

prompt = loads(json_data)

# Model
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.1)

# Chain
chain = prompt | model

# Invoke
response = chain.invoke({
    "question": "What is Machine Learning?"
})

print(response.content[0]["text"])