from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

'''
prompt = PromptTemplate(
    template="Explain {topic} to a {level} student.",
    input_variables=["topic", "level"]
)'''

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)

final_prompt = prompt.invoke({
    "topic": "Machine Learning"
})

response = model.invoke(final_prompt)

print(response.content[0]["text"])
