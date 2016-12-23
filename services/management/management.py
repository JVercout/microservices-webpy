from lib.application import WebApplication

urls = (
    '/?', 'Index'
)


class Index:
    def GET(self):
        return 'hello world'


app = WebApplication(urls, globals())
