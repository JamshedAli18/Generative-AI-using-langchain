from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def multiply1(a : int, b : int) -> int:
    """multiply two numbers"""
    return a * b

@tool
def multiply2(a : int, b : int, c: int) -> int:
    """multiply three numbers"""
    return a * b * c


model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

binded_llm = model.bind_tools([multiply1, multiply2])

# print((binded_llm.invoke("hi")))

result = binded_llm.invoke("I want you to mulpltiply 3 number 2,3 and 10")

print(multiply1.invoke(result.tool_calls[0]))


