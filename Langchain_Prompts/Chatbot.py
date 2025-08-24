from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage , AIMessage


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

chat_history = [
    SystemMessage(content='You are good assistant')
]

while True:
    user_input = input('YOU: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'quit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI Asssitant : " ,result.content)

print("Chatbot : " ,chat_history)
