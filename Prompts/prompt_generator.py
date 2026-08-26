from langchain_core.prompts import ChatPromptTemplate
from langchain_core.load import dumps

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher."),

    ("human", "What is Python?"),

    ("ai", "Python is a popular programming language."),

    ("human", "{question}")
])

json_data = dumps(prompt)

with open("my_prompt.json", "w", encoding="utf-8") as f:
    f.write(json_data)
