from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# define the response schema
schema = [
    ResponseSchema(name="name", description="The name of the person", type="string"),
    ResponseSchema(name="age", description="The age of the person", type="integer"),
]


# create structured output parser with the defined schema
parser = StructuredOutputParser.from_response_schemas(schema)

'''
prompt = PromptTemplate(
    template="Extract the person's name and age.\n{format_instructions}\nPerson: {text}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)'''

template = PromptTemplate.from_template(
    "Extract the person's name and age.\n{format_instructions}\nPerson: {text}"
)

# add the format instructions to the prompt template
prompt = template.partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser

if __name__ == "__main__":
    print(chain.invoke({"text": "Debabrata is 20 years old."}))