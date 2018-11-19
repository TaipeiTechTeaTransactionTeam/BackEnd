from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')(nnp=1cq*ty11n-75i8+@enp@xod_4qqem4*^p1u%47to2n+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

ALLOWED_HOSTS = ['http://35.234.8.158/','http://35.234.8.158/']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR,'my.cnf'),
        },
    }
}