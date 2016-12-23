import web
import json
from lib.application import WebApplication, token_authentication_processor
from lib.db import db

urls = (
    '/?', 'Index',
    '/alarm/?', 'Alarm'
)


class Index:
    def GET(self):
        web.header('Content-type', 'application/json')
        return json.dumps({"api_owner": "limmex", "api_version": "1.0", "db_thread": id(db.get_conn())})


class Alarm:
    def POST(self):
        web.header('Content-type', 'application/json')
        return json.dumps({'status': 'ko'})

app = WebApplication(urls, globals())
#app.add_processor(token_authentication_processor)
