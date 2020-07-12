from .base import *

DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

EMAIL_BACKEND = env("EMAIL_BACKEND")

DATABASES = {"default": env.db("DATABASE_URL")}
