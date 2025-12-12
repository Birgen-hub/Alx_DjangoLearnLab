# Social Media API - User Authentication

This project sets up the foundational user authentication system for a Social Media API using Django and Django REST Framework.

## Requirements

* Python 3.8+
* `pip install django djangorestframework`

## Setup & First Launch

1.  **Project Structure:** Ensure your file structure matches the project paths (e.g., `social_media_api/accounts/models.py`).

2.  **Database Migration:** Run the initial migrations to create the custom User model and the auth tables. (You must be in the directory containing `manage.py` for this to work.)
    ```bash
    python manage.py makemigrations accounts
    python manage.py migrate
    ```

3.  **Run Server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

All endpoints are prefixed with `/api/auth/`. The base URL is `http://127.0.0.1:8000/api/auth/`.

| Route | Method | Description | Authentication |
| :--- | :--- | :--- | :--- |
| `/register` | **POST** | Creates a new user account (returns token). | None |
| `/login` | **POST** | Authenticates a user and returns a token. | None |
| `/profile` | **GET/PATCH** | Manages the logged-in user's profile. | Token Auth |
