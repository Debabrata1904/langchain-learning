from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from prompt_toolkit import prompt

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

'''
prompt = PromptTemplate.from_template(
    """
    You are an expert Python teacher.

    Explain {topic} to a beginner.
    Use simple language.
    Give one real-world example.
    """
)

chain = prompt | model
response = chain.invoke({
    "topic": "Machine Learning"
})'''

prompt = PromptTemplate.from_template(
    """
    Explain {topic} for a {level} student.
    Give {examples} real-world examples.
    """
)

chain = prompt | model

response = chain.invoke({
    "topic": "RAG",
    "level": "beginner",
    "examples": 2
})

print(response.content[0]["text"])