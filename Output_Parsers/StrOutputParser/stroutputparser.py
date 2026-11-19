
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.8-27B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt template
prompt_template = PromptTemplate.from_template(
    "Write a detailed report on {topic}"
)

# 2nd prompt template
prompt_template2 = PromptTemplate.from_template(
    "Summarize the following text in 5 lines: {text}"
)

prompt1 = prompt_template.invoke({"topic": "black hole"})

response1 = model.invoke(prompt1)

prompt2 = prompt_template2.invoke({"text": response1.content[0]["text"]})

response2 = model.invoke(prompt2)

print("Response 1:", response2.content[0]["text"])