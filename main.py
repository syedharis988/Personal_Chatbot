from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Page config
st.set_page_config(page_title="Personal AI Chatbot", page_icon="🤖")

st.title("🤖 Personal AI Chatbot")

# Initialize model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Initialize chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful personal AI assistant.")
    ]

# Display previous messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)

    # Save user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Get AI response
    response = llm.invoke(st.session_state.messages)

    # Show response
    st.chat_message("assistant").write(response.content)

    # Save AI response
    st.session_state.messages.append(AIMessage(content=response.content))