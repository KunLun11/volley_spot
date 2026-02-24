import os
from pathlib import Path

import environ

env = environ.Env()

environ.Env.read_env(env.str("DOTENV_PATH", ".env"))

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = (BASE_DIR / "data").resolve()
STATIC_DIR = (DATA_DIR / "static").resolve()
TEMPLATE_DIR = (DATA_DIR / "templates").resolve()
LOG_DIR = (DATA_DIR / "logs").resolve()
MEDIA_DIR = (DATA_DIR / "media").resolve()

for directory in [DATA_DIR, STATIC_DIR, TEMPLATE_DIR, LOG_DIR, MEDIA_DIR]:
    os.makedirs(directory, exist_ok=True)

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1", "0.0.0.0"])

INSTALLED_APPS = [
    # UNFOLD
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    "unfold.contrib.location_field",
    "unfold.contrib.constance",
    # DJANGO
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # APPS
    "base",
    "account",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = "account.User"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
SERVE_STATIC = True

UNFOLD = {
    "SITE_TITLE": "VolleySpot - управление записями на игры",
    "SITE_HEADER": "VolleySpot админ",
    "SITE_SYMBOL": "sports_volleyball",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COMMAND": {
        "search_models": True,
        "search_callback": "utils.search_callback",
        "show_history": True,
    },
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
        },
    },
}
