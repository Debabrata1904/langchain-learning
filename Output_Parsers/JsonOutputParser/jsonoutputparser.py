from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    timeout=30,
    max_retries=2
)

# 1. Create parser
parser = JsonOutputParser()

'''
parser = JsonOutputParser()

template = PromptTemplate(
    template=(
        "Give me the name, age and city of a fictional person.\n"
        "{format_instruction}"
    ),
    input_variables=[],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)'''

# 2. Create prompt template
template = PromptTemplate.from_template(
    """Give me the name, age and city of a fictional person.

{format_instructions}"""
)

# 3. Add format instructions
prompt = template.partial(
    format_instructions=parser.get_format_instructions()
)

# 4. Create chain
chain = prompt | model | parser

# 5. Invoke chain
response = chain.invoke({})

print(response)
print(type(response))

#print(prompt.format())