# Django Template Project

A production-ready Django project template with modern best practices, custom user authentication, and Bootstrap 5 integration.

## Features

- **Custom User Model** with email-based authentication
- **Modular Settings** (base.py and prod.py configurations)
- **Bootstrap 5** with jQuery and Popper.js from CDN
- **Manifest Static Files Storage** for production cache-busting
- **Comprehensive .gitignore** for Django projects
- **Environment Variables** support with python-dotenv
- **Home App** with base templates ready for customization
- **Production-ready** logging and security configurations

## Quick Start

1. **Clone or download this template:**
   ```bash
   git clone https://github.com/qcif/django-template.git
   cd django-template
   ```

2. **Initialize your project:**
   ```bash
   ./init.sh
   ```
   This script will:
   - Prompt for your project name
   - Replace all instances of "myproject" with your project name
   - Rename directories appropriately
   - Update configuration files

3. **Set up your development environment:**
   ```bash
   cd your-project-name
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.sample .env
   # Edit .env with your settings
   ```

5. **Run migrations and create superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start development server:**
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
your-project-name/
├── accounts/                 # Custom user model app
│   ├── models.py            # Email-based User model
│   └── ...
├── home/                    # Home page app
│   ├── templates/home/      # Base templates
│   │   ├── header.html      # Base template with Bootstrap
│   │   └── index.html       # Homepage
│   └── ...
├── your-project-name/       # Main project directory
│   ├── settings/
│   │   ├── base.py          # Base settings
│   │   ├── prod.py          # Production settings
│   │   └── log/             # Logging configuration
│   ├── urls.py
│   └── wsgi.py
├── static/css/              # Static files
├── utils/                   # Utility modules
├── manage.py
├── requirements.txt
├── .env.sample              # Environment variables template
└── .gitignore
```

## Settings Configuration

### Development Settings (`base.py`)
- Uses SQLite database
- Debug mode enabled
- Development-friendly configurations
- Loads from `.env` file

### Production Settings (`prod.py`)
- Security headers enabled
- Manifest static files storage
- Production logging configuration
- SSL/HTTPS configurations

To use production settings:
```bash
export DJANGO_SETTINGS_MODULE=your_project_name.settings.prod
```

## Environment Variables

Copy `.env.sample` to `.env` and configure:

```bash
# Required
SECRET_KEY=your-secret-key-here
HOSTNAME=your-domain.com

# Email (optional)
MAIL_HOSTNAME=smtp.example.com
MAIL_SMTP_PORT=587
MAIL_SMTP_USERNAME=your-email@example.com
MAIL_SMTP_PASSWORD=your-password
MAIL_USE_TLS=true

# reCAPTCHA (optional)
RECAPTCHA_SITE_KEY=your-site-key
RECAPTCHA_SECRET_KEY=your-secret-key
```

## Custom User Model

The template includes a custom User model (`accounts.User`) that:
- Uses email as the username field
- Includes first_name, last_name fields
- Has proper UserManager for creating users and superusers
- Is properly configured in settings

## Frontend Framework

- **Bootstrap 5.3.0** loaded from CDN
- **jQuery 3.7.1** for enhanced functionality
- **Popper.js** for Bootstrap components
- **Local CSS** file for custom styles (`static/css/main.css`)

## Deployment

For production deployment:

1. Set environment variables appropriately
2. Use production settings: `your_project_name.settings.prod`
3. Run `python manage.py collectstatic`
4. Configure your web server (nginx/apache)
5. Use a WSGI server like Gunicorn