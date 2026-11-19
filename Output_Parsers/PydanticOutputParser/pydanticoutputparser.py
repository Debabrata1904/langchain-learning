from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

# Define e model
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# define e pydantic object
class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    country: str = Field(description="The country where the person lives")
    city: str = Field(description="The city where the person lives")

# define e pydantic output parser
parser = PydanticOutputParser(pydantic_object=Person)

# define e template
template = PromptTemplate.from_template(
    "Extract the name, age, and city from the following text: {text}\n{format_instructions}"
)
prompt = template.partial(format_instructions=parser.get_format_instructions())

# define e chain
chain = prompt | model | parser

# invoke the chain
response = chain.invoke({"text": "Debabrata Bhowmik is a 20-year-old Ai engineer living in India, Kolkata."})

# print the response
print("Response:", response)
