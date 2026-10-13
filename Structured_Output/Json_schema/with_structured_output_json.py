from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

review_schema = {
    "title":"Review",
    "description":"A schema for a product review",
    "type":"object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A list of key themes mentioned in the review"
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The sentiment of the review"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A list of positive aspects mentioned in the review"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A list of negative aspects mentioned in the review"
        },
        "name": {
            "type": "string",
            "description": "The full name of the person who wrote the review, not the product name"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}

    
structured_model = model.with_structured_output(review_schema)

result = structured_model.invoke(
    """The Vivo y21 5g is great,
    but the software is buggy and crashes frequently.
    Also the UI is look new. Camera quality is good,
    but this phone is lacking in performance.
    Overall, I am disappointed with the product.
    
    Review by Debabrata Bhowmik""" 
    )

print(result)