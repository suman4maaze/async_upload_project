
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%oxlsyl2g7vp#t+a1*bv=43zveohgb1s1+dvcc6)-44zwc8+*d'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'async_upload_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'file_upload.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'file_upload.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'TruckIndDB',
        #'NAME': os.getenv('db_name'),
        #'NAME': os.environ['NAME'],
        'NAME':'falcondbnew2022',
        #'NAME': 'dd21t9dbu9d5fc',
        #'NAME':'d31kkhodt6k2pd',
        #'USER':'dexwdojwynhgbo',
        #'USER':'gtyntnnumyrhdt',
        #'NAME': 'ins',
        #'USER':os.environ['USER'],
        'USER':'falconadmin',
        #'USER': os.getenv('db_user'),
        #'PASSWORD': '46e15532c5843dafdb7faeec89e7715389ae5693ddd434f95bcd596adfc05bc3',
        #'PASSWORD': os.environ['PASSWORD'],
        #'PASSWORD': 'Shamanth@1994',
        'PASSWORD':'Nta@2022$$!',
        #'PASSWORD': os.getenv('db_password'),
        #'HOST': 'ec2-3-224-157-224.compute-1.amazonaws.com',
        'HOST':'falcondbnew2022.postgres.database.azure.com',
        #'HOST':os.environ['HOST'],
        #'HOST': 'localhost',
        #'HOST': os.getenv('db_host'),
        'OPTIONS':{
        'sslmode':'require'
        },
        #'PORT':os.getenv('db_port')
        'PORT': '5432',
        
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
