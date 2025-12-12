# Social Media API (social_media_api)
This project provides a foundational Social Media API built with Django REST Framework.
## Setup and Launch
1. Ensure dependencies are installed: `pip install django djangorestframework`
2. Run the server: `python manage.py runserver`
## API Endpoints
| Endpoint | Method | Authentication | Description |
| :--- | :--- | :--- | :--- |
| `/api/v1/register` | POST | None | Create a new user account. |
| `/api/v1/login` | POST | None | Log in and receive an authentication token. |
| `/api/v1/profile` | GET/PUT | Token | Retrieve or update the authenticated user's profile. |
## Authentication
For protected endpoints (like `/profile`), include the token obtained during login in the request header:
`Authorization: Token <YOUR_TOKEN>`
