from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Initialize model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Store conversation history manually
chat_history = [
    SystemMessage(content="You are a helpful and friendly personal AI assistant. You remember the user and talk naturally.")
]

print("Personal AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Add user message to history
    chat_history.append(HumanMessage(content=user_input))

    # Get response
    response = llm.invoke(chat_history)

    # Add AI response to history
    chat_history.append(AIMessage(content=response.content))

    print("Bot:", response.content)