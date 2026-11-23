from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

# pydantic object
class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Sentiment)

template = PromptTemplate.from_template(
    "Classify the sentiment of the following feedback as positive, negative: {feedback}\n{format_instructions}"
)
prompt = template.partial(format_instructions=parser2.get_format_instructions())

pos_prompt = PromptTemplate.from_template(
    "Write an appropriate response to this positive feedback: {feedback}"
)

neg_prompt = PromptTemplate.from_template(
    "Write an appropriate response to this negative feedback: {feedback}"
)

sentiment_classifier_chain = prompt | model | parser2

chain1 = pos_prompt | model | parser
chain2 = neg_prompt | model | parser

# Preserve feedback and classify sentiment
parallel_chain = RunnableParallel({
    'feedback': RunnableLambda(lambda x: x["feedback"]),
    'sentiment': sentiment_classifier_chain
})

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', chain1),
    (lambda x:x.sentiment == 'negative', chain2),
    # default chain if no conditions match
    RunnableLambda(lambda x: "No appropriate response found.")
)

chain = sentiment_classifier_chain | branch_chain

print(chain.invoke({"feedback": "I love the new features in your software!"}))