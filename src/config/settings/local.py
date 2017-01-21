from .common import *

DEBUG = True

AUTH_PASSWORD_VALIDATORS = []

SECRET_KEY = 'j40y-h50zxE5ZCA0nmOXE1Cz_I9wAVExrIPz7ztPlKcC7p9XoMqIh53g-cJf_6o8emY'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'intent',
        'USER': 'intent',
        'PASSWORD': 'intent',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
