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

```text
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
```

## How It Works

1. Create an account using the Register page.
2. Login to your StudyMate AI account.
3. Open the Dashboard.
4. Select **AI Study Chat**.
5. Enter a study-related question.
6. StudyMate AI sends the question to the AI model.
7. The AI generates an explanation.
8. Previous questions and answers can be viewed in the chat history.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "StudyMate AI project"
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Do not upload your real API key to GitHub.

Make sure `.env` is included in `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## Run the Project

Start the Flask application:

```bash
python run.py
```

Then open the local address shown by Flask in your browser.

## Screenshots

Screenshots of the project interface can be added here.

### Login Page

![StudyMate AI Login](screenshots/login.png)

### Register Page

![StudyMate AI Register](screenshots/register.png)

### Dashboard

![StudyMate AI Dashboard](screenshots/dashboard.png)

### AI Study Chat

![StudyMate AI Chat](screenshots/ai-chat.png)

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
