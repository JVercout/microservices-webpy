# Microservices Framework

[![Build Status](https://travis-ci.org/JVercout/microservices-webpy.svg?branch=master)](https://travis-ci.org/JVercout/microservices-webpy)

## Requirements
 * Python 2.7.12
 * Pip manager

## Features:
 * Editor Configuration
 * Extensive Gitignore configuration
 * Continous Integration with Travis
 * Explicitly declare and isolate dependencies with virtualenv and pip management
 * Dynamic configuration according environment variable.
 * Independent web-services, based on web.py
 * Small, expressive ORM with Peewee
     * Independent database models, shared accross web threads and backgrounds tasks
     * Database Thread-Local Scope within Web application
       Source: http://docs.peewee-orm.com/en/latest/peewee/database.html#web-py
     * Database automatic reconnect
       Source: http://docs.peewee-orm.com/en/latest/peewee/database.html#automatic-reconnect
     * Database read-slave support (automatically run SELECT queries against one or more read replicas)
       Source: http://docs.peewee-orm.com/en/latest/peewee/database.html#read-slaves

 * Unit testing of web-services
 * Unit testing database model and operations
 * Run admin/management tasks as one-off processes.



## Todo
 * Federate application logging
    * Application event logging
    * Web application logging requests?
    * Celery tasks status
    * Database logging
      Source: http://docs.peewee-orm.com/en/latest/peewee/database.html#logging-queries
 * Celery tasks
    * Redis broker and backend
    * Routing queues according policy: support, alarm
    * Routing queues with different prefetch.
    * Celery database access, threaded with init and close database connection
      Source: http://www.prschmid.com/2013/04/using-sqlalchemy-with-celery-tasks.html
    * Celery single-tasks (distributed lock across worker)
    * Check reliability: CELERY_ACKS_LATE, CELERY_DISABLE_RATE_LIMITS, CELERYD_PREFETCH_MULTIPLIER=1
 * Unit testing queue management
 * Docopt create_table, migration support, celery workers, run web as production threads.
 * Critical settings (passphrases) can be overloaded through environment variables
 * Refactor testing coverage (through app folder?)
 * Continous Deployment (Docker eligible stack)
 * Database Schema Migration Support
   Source: http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#migrate
 * Better support for HTML, CSS, JS interfaces and backend APIs.
    * SASS Compilation
    * React.JS
    * Webpack


## Installation
```
git clone git@github.com:JVercout/microservices-webpy.git
cd microservices-webpy
pyenv virtualenv 2.7.12 microservices-webpy
pyenv local
pip install -r requirements/common.txt
# As developer, you could install developement.txt dependencies. 
```

## Usage
```
python manage.py

```

## Testing
```
pytest

```
