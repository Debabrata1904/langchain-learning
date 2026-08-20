from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "D:/huggingface"
os.environ["HF_HUB_CACHE"] = "D:/huggingface/hub"

# HuggingFace local pipeline
llm = HuggingFacePipeline(
    pipeline_name="text-generation",
    model_id="TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0",
    task="text-generation",

    # Generation parameters
    temperature=0.7,
    max_new_tokens=200,
    do_sample=True,
)

# Convert LLM into a LangChain chat model
chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("Explain machine learning in simple language.")

print(result.content)