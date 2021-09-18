import os

DJANGO_ENV_MODE = os.environ['DJANGO_ENV_MODE']

if DJANGO_ENV_MODE.lower() == 'dev':
    from .dev import *
elif DJANGO_ENV_MODE.lower() == 'prod':
    from .prod import *
else:
    raise EnvironmentError('No environment set. Please set DJANGO_ENV_MODE environment variable to `DEV` or `PROD`.')