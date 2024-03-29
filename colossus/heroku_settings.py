# flake8: noqa

from .production_settings import *

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

# Insert WhiteNoise middleware after SecurityMiddleware
security_middleware_index = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')

MIDDLEWARE.insert(security_middleware_index + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/public')

PRIVATE_MEDIA_ROOT = os.path.join(BASE_DIR, 'media/private')


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('smtp.mailgun.org')

EMAIL_PORT = config('25', cast=int)

EMAIL_HOST_USER = config('postmaster@sandbox8a157bd4fee247a9847ab3d12e41dbbe.mailgun.org')

EMAIL_HOST_PASSWORD = config('4aea5993a967cc60aa8138a55f1400b6-87cdd773-679d07b7')


# ==============================================================================
# LOGGING SETTINGS
# ==============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'colossus': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

CELERY_BROKER_READ_URL = config('CELERY_BROKER_READ_URL', default='')

CELERY_BROKER_WRITE_URL = config('CELERY_BROKER_WRITE_URL', default='')
