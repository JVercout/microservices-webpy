import web
from lib.application import token_authentication_processor

urls = ('/', 'index')


class index:
    def GET(self):
        return 'index_get'

    def POST(self):
        return 'index_post'


app = web.application(urls, globals())
app.add_processor(token_authentication_processor)

WWW_AUTHENTICATE_HEADER_CONTENT = 'Token realm="Limmex Watchgateway"'


def test_no_authentication():
    r = app.request('/', method='GET', headers=None)
    assert r.status == '401 Unauthorized'
    assert r.headers['WWW-Authenticate'] == WWW_AUTHENTICATE_HEADER_CONTENT

    r2 = app.request('/', method='POST', headers=None)
    assert r2.status == '401 Unauthorized'
    assert r2.headers['WWW-Authenticate'] == WWW_AUTHENTICATE_HEADER_CONTENT


def test_authentication_failed():
    authentication_headers = {'Authorization': 'Token wrong-token'}
    r = app.request('/', method='GET', headers=authentication_headers)
    assert r.status == '401 Unauthorized'
    assert r.headers['WWW-Authenticate'] == WWW_AUTHENTICATE_HEADER_CONTENT

    r = app.request('/', method='POST', headers=authentication_headers)
    assert r.status == '401 Unauthorized'
    assert r.headers['WWW-Authenticate'] == WWW_AUTHENTICATE_HEADER_CONTENT


def test_authentication_successful():
    authentication_headers = {'Authorization': 'Token aaa'}
    r = app.request('/', method='GET', headers=authentication_headers)
    assert r.status == '200 OK'
    assert r.data == 'index_get'

    r = app.request('/', method='POST', headers=authentication_headers)
    assert r.status == '200 OK'
    assert r.data == 'index_post'
