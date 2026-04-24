# Personal AI Chatbot

This is a small personal chatbot I built while learning LangChain and working with Groq API.
It runs in the terminal and can hold a conversation with you, remembering things during the session.

## What it does

* Lets you chat with an AI in the terminal
* Remembers previous messages in the same session
* Responds like a simple personal assistant

## Tech used

* Python
* LangChain
* Groq API

## How to run

Clone the repo:

```bash
git clone https://github.com/your-username/Personal_Chatbot.git
cd Personal_Chatbot
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install langchain langchain-groq python-dotenv
```

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

Type `exit` to stop the chatbot.

## Notes

* The chatbot memory is temporary (it resets when you stop the program)
* `.env` is ignored for security reasons

## Why I made this

Just practicing LangChain and understanding how chatbots with memory work.
Planning to improve it further with a UI and better memory.

## Next improvements

* Save chat history permanently
* Build a web interface
* Add more intelligent responses

If you find this useful or want to improve it, feel free to fork it.
