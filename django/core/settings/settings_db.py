from .settings import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {

    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "NAME": env("DB_NAME", default="cicd-testing"),
        "USER": env("DB_USER", default="cicd-testing"),
        "PASSWORD": env("DB_PASS", default="password"),
        "OPTIONS": {
            "options": "-c search_path=public"
        },
    },
    "cicd_testing_db": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "NAME": env("DB_NAME", default="cicd-testing"),
        "USER": env("DB_USER", default="cicd-testing"),
        "PASSWORD": env("DB_PASS", default="password"),
        "OPTIONS": {
            "options": "-c search_path=cicd_testing"
        },
    },
    "upload_db": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "NAME": env("DB_NAME", default="cicd-testing"),
        "USER": env("DB_USER", default="cicd-testing"),
        "PASSWORD": env("DB_PASS", default="password"),
        "OPTIONS": {
            "options": "-c search_path=upload"
        },
    },

}

DATABASE_ROUTERS = [
    'cicd_testing.routers.DatabaseRouter',
    'upload.routers.DatabaseRouter',

    'core.routers.db.AdminRouter',
    'core.routers.db.DefaultRouter',
]
