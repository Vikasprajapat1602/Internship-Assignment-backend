# 📘 Internship Assignment 

This project is developed using **Django**, **Django REST Framework**, **Celery**, **Redis**, and the **Telegram Bot API**. It includes secure JWT authentication, public/protected APIs, background task processing, and Telegram user data collection.

---

##  Features

-  Django project with REST APIs  
-  JWT-based authentication system  
-  Public & protected API endpoints  
-  Celery + Redis integration for async tasks  
-  Telegram bot that collects usernames  
-  Telegram data stored in Django model  
-  Admin panel for viewing Telegram users  

---

## Setup Instructions

### Clone the repository:

```bash
git clone https://github.com/Vikasprajapat1602/Internship-Assignment-backend.git
cd Internship-Assignment-backend
```

### Create virtual environment & install dependencies:

```bash
python -m venv venv
venv\Scripts\activate    # For Windows
pip install -r requirements.txt
```

### Create a `.env` file in the root directory:

```
SECURITY_KEY=your_django_secret_key
BOT_TOKEN=your_telegram_bot_token
```

---

## Running the Project Locally

>  Make sure Redis is installed and available in PATH

### 1. Start Redis Server

```bash
redis-server
```

### 2. Start Django development server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 3. Start Celery worker (new terminal)

```bash
celery -A backend worker --loglevel=info --pool=solo
```

### 4. Start Telegram bot (another terminal)

```bash
python telegram_bot.py
```

---

## API Endpoints

| URL                      | Method | Description              | Access      |
|--------------------------|--------|--------------------------|-------------|
| `/api/public/`           | GET    | Public API               | No auth     |
| `/api/protected/`        | GET    | Protected API            | JWT required|
| `/api/token/`            | POST   | Obtain access + refresh  | No auth     |
| `/api/token/refresh/`    | POST   | Refresh access token     | JWT required|

---

## 🤖 Telegram Bot

- Send `/start` to the bot to trigger username collection  
- The username is stored in the `TelegramUser` model  
- Accessible via Django admin panel  
- Built using `python-telegram-bot` (v20+)  

---

## Tech Stack

- Python 3.11+  
- Django 4.x  
- Django REST Framework  
- Celery  
- Redis  
- Telegram Bot API  
- SQLite (for development)  

---

## 📌 Notes

- `.env`, `venv/`, and `db.sqlite3` are excluded via `.gitignore`  
- Redis server must be running before starting Celery  
- Designed for internship evaluation, easy to extend
