from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

loader = TextLoader('ai.txt')

docs = loader.load()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template='Generate a short summary of given poem /n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt1 | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)

# print(type(docs))
# print(docs)
#
# print(docs[0])
#
# print(docs[0].page_content)
