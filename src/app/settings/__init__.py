from pathlib import Path

from split_settings.tools import include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4h5q3x08+6au55(pwbg5$t@0vhtq18zg)@htzqwmyjnx-4n65i"

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = "app.urls"

WSGI_APPLICATION = "app.wsgi.application"

include(
    "environ.py",
    "auth.py",
    "celery.py",
    "db.py",
    "email.py",
    "i18n.py",
    "installed_apps.py",
    "middleware.py",
    "restframework.py",
    "static.py",
    "templates.py",
)
