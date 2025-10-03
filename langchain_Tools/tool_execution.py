from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def multiply(a : int, b : int) -> int:
    """multiply two numbers"""
    return a * b



llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('can you multiply 3 with 1000')

messages = [query]

# print(messages)

result = llm_with_tools.invoke(messages)

# print(result)

messages.append(result)

# print(messages)
tool_result = multiply.invoke(result.tool_calls[0])

# print(tool_result)

messages.append(tool_result)

final_output = llm_with_tools.invoke(messages).content

print(final_output)
