# CAPERSMED Web Application

Premium Django web application for CAPERSMED.SARL, a Moroccan gourmet food producer.

## Tech Stack
- Backend: Django 4.2+
- Frontend: HTML5, CSS3, Vanilla JavaScript with GSAP
- Database: SQLite (Development) / PostgreSQL (Production)
- Deployment: Compatible with Render/Railway/Heroku

## Features
- Fully responsive Apple-inspired design with Moroccan cultural touches.
- Multi-language support (English, French, Arabic with RTL support).
- Premium GSAP ScrollTrigger animations.
- Dynamic product management via Django Admin.
- Built-in SEO optimizations.
- Working contact form with email notifications.
- WhatsApp floating widget.

## Setup Instructions

1. **Clone and Setup Virtual Environment:**
   ```bash
   git clone <repository_url> capersmed
   cd capersmed
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   - Copy `.env.example` to `.env`.
   - Update values (e.g., `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).

4. **Database & Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load Fixtures (Sample Data):**
   ```bash
   python manage.py loaddata products.json
   ```

6. **Create Superuser (for Admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## Deployment (Heroku/Render)
This project uses `whitenoise` for static files serving and a `Procfile` is included for automatic discovery by platforms like Heroku and Render.

- Ensure you set `DEBUG=False` and `ALLOWED_HOSTS` in production environment variables.
- Configure `DATABASE_URL` for PostgreSQL.
