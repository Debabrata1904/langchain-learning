from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1= PromptTemplate.from_template("Generate a detailed report about {topic}.")

prompt2 = PromptTemplate.from_template("Summarize the report in 3 bullet points. \nReport: {report}")

# Create a Google Generative AI chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()

chain1 = prompt1 | chat_model | parser | prompt2 | chat_model | parser

response = chain1.invoke({"topic": "space exploration"})

print("Response:", response)