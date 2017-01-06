import os
import web
import pytest
from lib.application import WebApplication
from lib.db import db


class index:
    def GET(self):
        return id(db.get_conn())


@pytest.fixture
def app():
    urls = ('/', 'index')

    current_env = os.environ['MICROSERVICES_SETTINGS']
    os.environ['MICROSERVICES_SETTINGS'] = 'settings.test'
    return WebApplication(urls, globals())
    os.environ['MICROSERVICES_SETTINGS'] = current_env


def test_database_processor(app):
    r = app.request('/')
    assert r.status == '200 OK'
    assert r.data.isdigit()


def test_database_session_local_thread(app):
    r1 = app.request('/')
    assert r1.status == '200 OK'
    assert r1.data.isdigit()

    r2 = app.request('/')
    assert r2.status == '200 OK'
    assert r1.data != r2.data


def test_config_loaded(app):
    assert web.config.debug is True
