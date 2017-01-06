import os

settings_path = None
if 'MICROSERVICES_SETTINGS' in os.environ:
    settings_path = os.environ['MICROSERVICES_SETTINGS']
else:
    settings_path = 'settings.dev'

if settings_path == 'settings.dev':
    from settings.dev import *
elif settings_path == 'settings.test':
    from settings.test import *
elif settings_path == 'settings.prod':
    from settings.prod import *
else:
    raise RuntimeError('Error while loading settings')
