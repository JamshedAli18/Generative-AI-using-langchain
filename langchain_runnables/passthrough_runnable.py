from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a funny joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the meaning of following joke in short and simple - {text}",
    input_variables=['text']
)


joke_geneartor = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2,model,parser)
})

final_chain = joke_geneartor | parallel_chain

result = final_chain.invoke({'topic':'AI'})

print(result)
