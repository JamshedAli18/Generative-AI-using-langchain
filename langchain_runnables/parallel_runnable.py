from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="generate a tweet about {topic} for twitter",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate content about {topic} for linkedin post",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(prompt1,model,parser),
    "linkedin post" : RunnableSequence(prompt2,model,parser),
})

result = parallel_chain.invoke({"topic": "AI"})


print(result['tweet'])
print(result['linkedin post'])
