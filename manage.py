import web
from services.management import management
from services.watchgateway import watchgateway
web.config.debug = True

urls = (
    '/management', management.app,
    '/watchgateway', watchgateway.app,
)


app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()
