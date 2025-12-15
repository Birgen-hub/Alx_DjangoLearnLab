# Deployment Plan and Documentation for Social Media API

This document outlines the strategy for deploying the `social_media_api` Django REST project to a production environment.

**Selected Hosting Service:** Heroku (or similar platform requiring Gunicorn/WhiteNoise)

## 1. Prerequisites

Before deployment, ensure you have:
1.  A hosting account (e.g., Heroku, DigitalOcean, AWS).
2.  The Heroku CLI installed (if using Heroku).
3.  All code committed and pushed to your GitHub repository (`Alx_DjangoLearnLab`).

## 2. Project Preparation

The following configuration files have been created/modified to support production:

| File | Purpose | Key Changes |
| :--- | :--- | :--- |
| `requirements.txt` | Lists all dependencies, including `gunicorn` and `whitenoise`. | Added deployment dependencies. |
| `Procfile` | Specifies the command to run the web server. | `web: gunicorn social_media_api.wsgi` |
| `social_media_api/social_media_api/settings.py` | Configures production security and resources. | `DEBUG = False`, `ALLOWED_HOSTS` via ENV, `WhiteNoiseMiddleware`, `SECURE_*` headers, `dj_database_url` setup. |

## 3. Deployment Steps (Example: Heroku)

### A. Environment Setup

1.  **Create App:**
    ```bash
    heroku create <app-name>
    ```
2.  **Set Environment Variables:** Configure your critical security variables.
    ```bash
    heroku config:set DJANGO_SECRET_KEY='<Your_Strong_Secret_Key>'
    heroku config:set ALLOWED_HOSTS='<app-name>.herokuapp.com'
    heroku config:set DJANGO_DEBUG='False'
    # Optional: If you use S3 for media files, set credentials here
    ```
3.  **Database Provisioning:** Heroku automatically provides a PostgreSQL database via the `DATABASE_URL` environment variable, which `settings.py` is configured to use.

### B. Deployment & Finalization

1.  **Push to Heroku Git Remote:**
    ```bash
    git push heroku master
    ```
2.  **Run Migrations:** Apply database migrations on the live server.
    ```bash
    heroku run python social_media_api/manage.py migrate
    ```
3.  **Collect Static Files:** WhiteNoise is configured to handle static files, but Django still needs to collect them into the `staticfiles` directory.
    ```bash
    heroku run python social_media_api/manage.py collectstatic --noinput
    ```

## 4. Live URL and Verification

**Live URL:**
*(Since this is a simulated environment, I cannot provide a live URL. After successful deployment, the URL will be provided by your hosting service, e.g., `https://<app-name>.herokuapp.com/`)*

**Final Testing Endpoints:**
* **Health Check:** `https://<live-url>/auth/login/` (Should return a method not allowed error, confirming Django is running).
* **Register:** `https://<live-url>/auth/register/` (Use POST with JSON data).
* **Feed:** `https://<live-url>/api/feed/` (Requires Authorization: Token header).

## 5. Maintenance and Monitoring Plan

1.  **Logging:** Use the hosting platform's built-in logging tools (e.g., Heroku Logs) to monitor errors and application health. Set up Sentry or similar external error tracking for production alerts.
2.  **Security Updates:** Regularly review the `requirements.txt` and update dependencies, especially Django and Django REST Framework, to patch security vulnerabilities.
3.  **Database Backups:** Ensure the production database (e.g., PostgreSQL) has automatic backup enabled by the hosting provider.
4.  **Static Files:** If user-uploaded media files are implemented, transition from local storage to a cloud storage service like AWS S3 or DigitalOcean Spaces for scalability and persistence.
