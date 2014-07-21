# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ks_m)focn2e_*9!@i0+1g+poy&#l32yz0xstt+*o3lp9@r1prc'

#--------------------APLICACIONES-------------------------------#
#Apps del framework:
DJANGO_APPS = (
    'django_admin_bootstrapped', #Bootstrap en el administrador
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

#Apps de terceros:
THIRD_PARTY_APPS = ( 
	'south', # migraciones en base de datos
	'social.apps.django_app.default', # login con social auth
    'djrill', # permite conectar el proyecto con Mandrill.     
	)
#Apss propias
LOCAL_APPS = (
	'apps.home',
    'apps.farma',
    'apps.bible',
	'apps.users', # User Custom Model
    'apps.ejemplos',
	)

#Tupla con todas las aplicaciones definidas en el proyecto:
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Backends.urls'

WSGI_APPLICATION = 'Backends.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Ruta hacia los archivos ".html"
TEMPLATE_DIRS = [BASE_DIR.child('templates')]

#Atributo que determina que modelo de usuario personalizado usaremos:
AUTH_USER_MODEL = 'users.User'

#-------------------VARIABLES PARA SOCIAL LOGIN----------------#

#Determina que tipo de autenticacion vamos a utilizar
AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookAppOAuth2',
	'social.backends.facebook.FacebookOAuth2',
	'social.backends.twitter.TwitterOAuth',
	'django.contrib.auth.backends.ModelBackend',
	)

#Determina a donde dirigirse luego de hacer login:
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/extra-data/' 

#Determina a donde dirigirse si hay error en el logueo:
SOCIAL_AUTH_LOGIN_URL = '/error/'

#Determina que modelo de usuarios vamos a utilizar:
SOCIAL_AUTH_USER_MODEL = 'users.User'

#Variable que permite que facebook retorne el email del usuario logueado. 
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

#Funciones para autentificacion (Social Auth Avanzado)
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    #Funcion para traer el avatar del user
    'apps.users.pipelines.get_avatar',
    )

#Especificamos el servicio de emailing que vamos a usar. En este caso, mandrill. 
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
