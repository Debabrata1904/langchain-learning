from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(TypedDict):
    key_themes: Annotated[list[str], "A list of key themes mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "The sentiment of the review"]
    pros: Annotated[Optional[list[str]], "A list of positive aspects mentioned in the review"]
    cons: Annotated[Optional[list[str]], "A list of negative aspects mentioned in the review"]
    name: Annotated[Optional[str], "The full name of the person who wrote the review, not the product name"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """The Vivo y21 5g is great,
    but the software is buggy and crashes frequently.
    Also the UI is look new. Camera quality is good,
    but this phone is lacking in performance.
    Overall, I am disappointed with the product.
    
    Review by Debabrata Bhowmik""" 
    )

print(result)