from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

class Review(BaseModel):
    key_themes: list[str] = Field(description="A list of key themes mentioned in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="The sentiment of the review")
    pros: Optional[list[str]] = Field(default=None, description="A list of positive aspects mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="A list of negative aspects mentioned in the review")
    name: Optional[str] = Field(default=None, description="The full name of the person who wrote the review, not the product name")

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
#print(result.model_dump_json())