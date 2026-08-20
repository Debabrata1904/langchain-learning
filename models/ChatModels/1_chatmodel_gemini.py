from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    #temperature=0.7,
    #max_output_tokens=1024,
    #top_k=40,
    #top_p=0.95,
)

result = chat_model.invoke("Explain machine learning in simple language.")

#print(result.content)

print(result.content[0]["text"])