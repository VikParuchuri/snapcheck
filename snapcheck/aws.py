from settings import *
import json

with open(ENV_ROOT / "env.json") as env_file:
    ENV_TOKENS = json.load(env_file)

with open(ENV_ROOT / "auth.json") as auth_file:
    AUTH_TOKENS = json.load(auth_file)

DEBUG = False

DATABASES = AUTH_TOKENS.get('DATABASES', DATABASES)
allowed_hosts = ENV_TOKENS.get('ALLOWED_HOSTS')
if allowed_hosts is not None:
    ALLOWED_HOSTS += allowed_hosts

SECRET_KEY = AUTH_TOKENS.get('SECRET_KEY', SECRET_KEY)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}
