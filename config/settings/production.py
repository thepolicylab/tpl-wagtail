from __future__ import absolute_import, unicode_literals

from .base import *

import os 

env = os.environ.copy()
#SECRET_KEY = env['SECRET_KEY']
#SECRET_KEY = 'ababbababa'
SECRET_KEY = '5+f#!xn=hj^u#=cr9@pz@@5cf7bqf0ymy=8uyfpx_zvxpght3='


DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = (
    ('Charlene Wang', 'hsinlei.w@gmail.com'),
)


ALLOWED_HOSTS = ['plabextcmscit.services.brown.edu', 'localhost']

#STATIC_URL = '/static/'

try:
    from .local import *
except ImportError:
    pass
