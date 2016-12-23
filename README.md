# Microservices Framework

## Requirements
 * Python 2.7.12
 * Pip manager

## Features:
 * Editor Configuration
 * Extensive Gitignore configuration
 * Explicitly declare and isolate dependencies with virtualenv and pip mangement
 * Dynamic confgiuration according an envrionment variable. 
 * Independent web-services, based on web.py.
 * Small, expressive ORM with Peewee
 * MySQL database backend
    * Automatic Reconnect behavior if a query failed with OperationalError
 * Independent database models, shared accross web threads and backgrounds tasks
 * Database Thread-Local Scope within Web application
   Source: http://docs.sqlalchemy.org/en/rel_1_1/orm/contextual.html#using-thread-local-scope-with-web-applicationsr
 * Unit testing of web-services
 * Unit testing database layer (models & operations)


## Todo
 * Application logging
    * Application event logging
    * Web application logging requests?
    * Celery tasks status
 * Celery tasks
    * Redis broker and backend
    * Celery database access, threaded with init and close database connection http://www.prschmid.com/2013/04/using-sqlalchemy-with-celery-tasks.html
    * Celery single-tasks (lock across worker)
 * Run admin/management tasks as one-off processes
 * Load critical settings (passphrases) through environment variables (overload)
 * MySQL
    * Read_slaves
 * Refactor testing coverage (through app folder?)
 * Integration testing
 * Acceptance tests accross microservices

## Installation
```
git clone git@github.com:JVercout/microservices-webpy.git
cd microservices-webpy
pyenv virtualenv 2.7.12 microservices-webpy
pyenv local
pip install -r requirements/common.txt
# As developer, you could install dev.txt dependencies. 
```

## Usage
```
python manage.py

```

## Testing
```
pytest

```
