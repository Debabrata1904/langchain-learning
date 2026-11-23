from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("Generate 5 interesting facts about {topic}.")

# Create a Google Generative AI chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

parser = StrOutputParser()

chain = prompt | chat_model | parser

response = chain.invoke({"topic": "space exploration"})

print("Response:", response)

# chain.get_graph().print_ascii()  # visualize the chain graph