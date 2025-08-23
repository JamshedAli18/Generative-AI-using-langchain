import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=200
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("tell me about the history of the internet in five lines")

print(response.content)



