from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)09@t=xvu!dss2o@s3zvzgcfmp6asi=rlro2rvqpu&=p!c1s8q'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    'django_filters',
    'bu_bo_app',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'BulletinBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'BulletinBoard.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC_ROOT = 'static/' # STATIC_ROOT и STATICFILES_DIRS не должны быть одинаковым путем.Для полей типа FileField
STATIC_URL = '/static/'

MEDIA_ROOT = 'media/'  # название папки, где хранятся медиа-данные.
MEDIA_URL = '/media/'  # путь для веб-сервера

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # стиль

        # регистрация
LOGIN_REDIRECT_URL = "/articles"
LOGOUT_REDIRECT_URL = "/accounts/login"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # встроенный бэкенд Django реализующий аутентификацию по username
    'allauth.account.auth_backends.AuthenticationBackend', # бэкенд аутентификации, предоставленный пакетом allauth
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # верификация включена, чтобы зарегица, нужно пройти по ссылке из письма

#Чтобы allauth распознал нашу форму как ту,что должна выполняться вместо формы по умолчанию
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

                #Настройка почты
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # письмо придет на почту
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # письмо придет в консоль
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "karlusha.zarazniy@yandex.ru"
EMAIL_HOST_PASSWORD = "vzyohuyxqxdxvvti"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "karlusha.zarazniy@yandex.ru"

SITE_URL = 'http://127.0.0.1:8000'

# указывает на URL брокера сообщений (Redis).По умолчанию на порту 6379. redis for celery
CELERY_BROKER_URL = 'redis://default:qzlMZ2VRlhtk61iac7rlpzsdqJvs9hmb@redis-17053.c61.us-east-1-3.ec2.cloud.redislabs.com:17053'
# указывает на хранилище результатов выполнения задач.
CELERY_RESULT_BACKEND = 'redis://default:qzlMZ2VRlhtk61iac7rlpzsdqJvs9hmb@redis-17053.c61.us-east-1-3.ec2.cloud.redislabs.com:17053'
CELERY_ACCEPT_CONTENT = ['application/json'] # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json' # метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json' # метод сериализации результатов.

CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_TASK_TIME_LIMIT = 30*60 # время жизни таски