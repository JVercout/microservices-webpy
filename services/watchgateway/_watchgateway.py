import web
import random
import string
import json
from lib.application import WebApplication, token_authentication_processor
from lib.models import User

urls = (
    '/?', 'Index',
    '/add', 'Add',
    '/view', 'View'
)


class Index:
    def GET(self):
        return 'hello world'


class Add:
    def GET(self):
        web.header('Content-type', 'text/html')
        fname = "".join(random.choice(string.letters) for i in range(4))
        lname = "".join(random.choice(string.letters) for i in range(7))
        u = User(
            name=fname,
            fullname=fname + ' ' + lname,
            password='542')
        u.save()
        return "added:" + web.websafe(str(u)) \
                        + "<br/>" \
                        + '<a href="/view">view all</a>'


class View:
    def GET(self):
        web.header('Content-type', 'application/json')
        return map(json.dumps, User.select().dicts())


app = WebApplication(urls, locals())
app.add_processor(token_authentication_processor)
