from .base import *

DEBUG = True
ALLOWED_HOSTS=[]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')] # indicando la carpeta static que ahi estara los archivos estaticos

#para direccionar las imagenes:
MEDIA_URL ='/media/'
MEDIA_ROOT = BASE_DIR.child('media')
# y para que reconozca las urls de las imagenes se debe configurar la ruta en url de general del proyecto en settings