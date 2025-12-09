# Learning Log

A simple web application built with Django that allows users to keep a log of topics they are learning about and make entries for each topic.

## Features

- **User Accounts**: Secure user registration and authentication.
- **Topics**: Users can create private topics they are interested in.
- **Entries**: Add detailed logs/entries for specific topics.
- **Privacy**: Topics and entries are private to the user who created them.

## Technology Stack

- **Backend**: Python 3, Django 4.0
- **Frontend**: Django Templates, Bootstrap 4
- **Database**: SQLite (default)

## Setup & Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000`.

## Notes

- This project is compatible with Python 3.13 (uses `legacy-cgi` for Django 4.0 compatibility).
