"""
Microservices Framework

A microframework to build up solid independant services.
Web-services offer the opportunity to make callable services.
Services communicates between each other based on queue system.

The framework allows you to implement your own policy in case of
messages processing failure, or when component you rely on are down.

Usage:
    manage.py devserver [-p NUM]

Options:
    -p NUM --port=NUM       Port number to launch the application
                            [default: 5000]

"""
import sys
import web
import signal
from functools import wraps
from docopt import docopt
from services.management import management
from services.watchgateway import watchgateway

OPTIONS = docopt(__doc__) if __name__ == '__main__' else dict()


def command(func):
    """Decorator that registers the chosen command/function.

    If a function is decorated with @command but that function name is not a valid "command" according to the docstring,
    a KeyError will be raised, since that's a bug in this script.

    If a user doesn't specify a valid command in their command line arguments, the above docopt(__doc__) line will print
    a short summary and call sys.exit() and stop up there.

    If a user specifies a valid command, but for some reason the developer did not register it, an AttributeError will
    raise, since it is a bug in this script.

    Finally, if a user specifies a valid command and it is registered with @command below, then that command is "chosen"
    by this decorator function, and set as the attribute `chosen`. It is then executed below in
    `if __name__ == '__main__':`.

    Doing this instead of using Flask-Script.

    Positional arguments:
    func -- the function to decorate
    """
    @wraps(func)
    def wrapped():
        return func()

    # Register chosen function.
    if func.__name__ not in OPTIONS:
        raise KeyError('Cannot register {}, not mentioned in docstring/docopt.'.format(func.__name__))
    if OPTIONS[func.__name__]:
        command.chosen = func

    return wrapped


@command
def devserver():
    urls = (
        '/management', management.app,
        '/watchgateway', watchgateway.app,
    )
    app = web.application(urls, locals())
    web.httpserver.runsimple(
        app.wsgifunc(),
        ('0.0.0.0', int(OPTIONS['--port']))
    )

# TODO:
# Create tables
# Execute migrations
# Launch celery worker
# Launch prod: web & celery


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))  # Properly handle Control+C
    if not OPTIONS['--port'].isdigit():
        print('ERROR: Port should be a number.')
        sys.exit(1)
    getattr(command, 'chosen')()
