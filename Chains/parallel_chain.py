from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model1 = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

model2 = ChatGroq(model="openai/gpt-oss-120b")

prompt1= PromptTemplate.from_template("Generate short and simpl notes from the following text: \n{text}")

prompt2= PromptTemplate.from_template("Generate 5 short questions from the following text: \n{text}")

prompt3= PromptTemplate.from_template("Merge the provided notes and questions into a single document: \nNotes: {notes} \nQuestions: {questions}")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'questions': prompt2 | model2 | parser,
})

marge_chain = prompt3 | model1 | parser

chain = parallel_chain | marge_chain

text = """
Artificial Intelligence is a branch of computer science.
It enables machines to perform tasks that normally require
human intelligence. Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.
"""

response = chain.invoke({'text' : text})

print("Response: ",response)