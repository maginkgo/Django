#Importamos el setting "base.py"
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#---------------------BASE DE DATOS--------------------------#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'BaseDatos',
        'USER': 'maginkgo',
        'PASSWORD': '13987',        
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Especificamos la ruta para los archivos estaticos:
STATICFILES_DIRS = [BASE_DIR.child('static')]


#LOGIN SOCIAL AUTH
SOCIAL_AUTH_FACEBOOK_KEY = '1417097368568950'
SOCIAL_AUTH_FACEBOOK_SECRET = '76b26752686f18bda3c923c6fbbad1c8'

SOCIAL_AUTH_TWITTER_KEY = '9tKD0TQwiyK62GnOrqgNHLrQO'
SOCIAL_AUTH_TWITTER_SECRET = 'jyS39eDEPlujlUNQOAJ9NEhlBpG5wX1g0V1gTpQKNKLovmgimw'

MANDRILL_API_KEY = "5tawkFIR9JiKaw4sG4ZNqQ"