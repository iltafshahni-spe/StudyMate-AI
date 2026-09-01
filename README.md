# StudyMate AI

StudyMate AI is a web-based AI Study Assistant built with **Python, Flask, SQLAlchemy, HTML, CSS, and Mistral AI**.

It helps students study more effectively by allowing them to ask questions and receive AI-powered explanations through a simple and modern interface.

## Features

* User Registration
* User Login and Logout
* Secure Session-Based Authentication
* AI Study Chat
* AI-powered answers and explanations
* Chat History
* Database Integration with SQLAlchemy
* Modern and Responsive UI
* Flask Blueprint-based project structure

## Technologies Used

* Python
* Flask
* SQLAlchemy
* SQLite / SQL Database
* HTML5
* CSS3
* JavaScript
* LangChain
* Mistral AI API
* Pydantic
* python-dotenv

## Project Structure


StudyMate AI/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   └── ai.py
│   │
│   ├── services/
│   │   └── ai_services.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── chat.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── models.py
│   └── __init__.py
│
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md

## How It Works

1. Create an account using the Register page.
2. Login to your StudyMate AI account.
3. Open the Dashboard.
4. Select **AI Study Chat**.
5. Enter a study-related question.
6. StudyMate AI sends the question to the AI model.
7. The AI generates an explanation.
8. Previous questions and answers can be viewed in the chat history.



## Future Improvements

* AI-generated study summaries
* AI flashcards
* Personalized learning plans
* Better chat memory
* Study progress tracking
* More AI-powered learning tools

## Author

**Iltaf Hussain**

Built as a learning project to practice Flask, databases, APIs, LangChain, and Generative AI integration.
