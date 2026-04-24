# Personal AI Chatbot

This is a simple personal AI chatbot I built while learning LangChain and working with the Groq API.

It started as a terminal-based chatbot, and now also includes a basic web interface using Streamlit.

## What it does

* Chat with an AI assistant
* Remembers conversation during the session
* Works in both:

  * Terminal (CLI)
  * Web UI (Streamlit)

## Tech used

* Python
* LangChain
* Groq API
* Streamlit

## How to run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Personal_Chatbot.git
cd Personal_Chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

## Run the chatbot

### ▶️ Terminal version

```bash
python main.py
```

### 🌐 Web UI version

```bash
python -m streamlit run app.py
```

Then open:

```
http://localhost:8501
```

## Notes

* Chat memory is temporary (resets when app restarts)
* `.env` is ignored for security
* Built mainly for learning and practice

## Future plans

* Save chat history permanently
* Improve UI design
* Deploy it online

## Why I made this

I built this project to understand how modern AI chat systems work and to get hands-on experience with LangChain.

If you find this useful or want to improve it, feel free to fork it.
