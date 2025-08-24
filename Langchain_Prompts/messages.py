from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

# from Langchain_Prompts.Chatbot import result

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

messages = [
    SystemMessage(content='You are good assistant'),
    HumanMessage(content='Tell me about youself in one line')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
