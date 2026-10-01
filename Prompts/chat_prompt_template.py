from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful {role} expert."),
        ("human", "Explain the concept of {concept} in simple terms."),
    ]
)

prompt = chat_prompt.invoke({
    'role': 'AI Engineer',
    'concept': 'Retrieval Augmented Generation (RAG)'
})

print(prompt)