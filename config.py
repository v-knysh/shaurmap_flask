import os
basedir = os.path.abspath(os.path.dirname(__file__))

from keys import MYSQL_PASSWORD, SECRET_KEY

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:{0}@localhost/shaurmap_db'.format(MYSQL_PASSWORD)

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


CSRF_ENABLED = True
