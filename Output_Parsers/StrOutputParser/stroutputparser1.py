from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    timeout=30,
    max_retries=2
)

# 1st prompt template
prompt_template = PromptTemplate.from_template(
    "Write a detailed report on {topic}"
)

# 2nd prompt template
prompt_template2 = PromptTemplate.from_template(
    "Summarize the following text in 5 lines: {text}"
)

parser = StrOutputParser()

chain = prompt_template | model | parser | prompt_template2 | model | parser

response = chain.invoke({"topic": "black hole"})

print("Response:", response)
