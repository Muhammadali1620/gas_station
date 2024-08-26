from django.conf import settings


LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
    ('en', 'English'),
]
MODELTRNSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRNSLATION_LANGUAGE = ('ru', 'en', 'uz')

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]