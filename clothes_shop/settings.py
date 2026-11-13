from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-local-clothes-lab"
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ROOT_URLCONF = "clothes_shop.urls"
WSGI_APPLICATION = "clothes_shop.wsgi.application"
LANGUAGE_CODE = "ru"
TIME_ZONE = "Asia/Yekaterinburg"

INSTALLED_APPS = ["django.contrib.staticfiles", "catalog"]
MIDDLEWARE = ["django.middleware.csrf.CsrfViewMiddleware"]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]
STATIC_URL = "/static/"
