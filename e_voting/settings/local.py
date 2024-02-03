from .base import *

DATABASES = {
    #   You can use this :
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'e_voting',
    #     'HOST': '127.0.0.1',
    #     'USER': 'root',
    #     'PASSWORD': ''
    # }
}