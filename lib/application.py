import re
import web
import settings
from lib.models import db


class WebApplication(web.application):
    """
        WebApplication
        Precessor connection with database
        Configuration loading
    """
    def __init__(self, mapping, fvars, autoreload=None):
        web.config.debug = settings.DEBUG
        web.application.__init__(self, mapping, fvars, autoreload)
        self.add_processor(connection_processor)


def connection_processor(handler):
    db.connect()
    try:
        return handler()
    finally:
        if not db.is_closed():
            db.close()


tokens = ('aaa')


def token_authentication_processor(handler):
    """
        Basic Token Authentication
        Authenticate a request with a predefined token per device
    """
    auth = web.ctx.env.get('HTTP_AUTHORIZATION')
    authreq = False
    if auth is None:
        authreq = True
    else:
        token = re.sub('^Token ', '', auth)
        if token in tokens:
            return handler()
        else:
            authreq = True

    if authreq:
        web.header('WWW-Authenticate', 'Token realm="Limmex Watchgateway"')
        web.ctx.status = '401 Unauthorized'
        return
