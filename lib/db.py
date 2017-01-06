import settings
from playhouse.db_url import connect

if 'default' in settings.DATABASES:
    if 'URI' in settings.DATABASES['default']:
        db = connect(settings.DATABASES['default']['URI'])
    else:
        raise RuntimeError('No URI defined for the default database')()
else:
    raise RuntimeError('No default database defined')
