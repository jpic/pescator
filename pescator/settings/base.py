# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf.global_settings import *

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'modeltranslation',
    'django_extensions',
    'redactor',
    'pages',
    'guestbook',
    'bootstrapform',
    'south',
    'sortedm2m',
    'easy_thumbnails',
    'autocomplete_light',
    'compressor',
    'reversion',
    'yourlabs',
    'pescator',
    'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'yourlabs.context_processors.expose_settings',
    'pescator.context_processors.menu',
)

EXPOSE_SETTINGS = ('DEBUG', 'COMPRESS_ENABLED')

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')

MODELTRANSLATION_CUSTOM_FIELDS = ('RedactorField',)


def project_directory(*join):
    return os.path.realpath(
        os.path.join(PROJECT_ROOT, *join).replace('\\', '/'))

# {{{ django-compressor stuff
COMPRESS_PRECOMPILERS = (
    ('text/less', 'recess --compile {infile} --compress > {outfile}'),
    ('text/coffeescript', 'coffee --compile --stdio'),
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.CSSMinFilter',
)
# }}}

# {{{ Internationalization stuff
gettext = lambda s: s
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Paris'
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('fr', gettext('Français')),
    ('en', gettext('English')),
)
# }}}

# {{{ FS and HTTP server static/media configuration
LOCALE_PATHS = (project_directory('locale'),)
MEDIA_ROOT = project_directory('public/media')
MEDIA_URL = '/public/media/'
STATIC_ROOT = project_directory('public/static')
STATIC_URL = '/public/static/'
STATICFILES_DIRS = (project_directory('static'),)
TEMPLATE_DIRS = (project_directory('templates'),)
FIXTURE_DIRS = (project_directory('fixtures'),)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': project_directory('whoosh_index'),
    },
}
# }}}

SITE_ID = 1
SECRET_KEY = '^7x4mu!cdsjj-*!gv&#@2g$d7&lfp#7_)gi4n30yd^vewaak*3'
ROOT_URLCONF = 'pescator.urls'
WSGI_APPLICATION = 'pescator.wsgi.application'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'pescator.yourlabs.org']
