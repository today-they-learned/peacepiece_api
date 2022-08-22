import dj_database_url

from .base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

ALLOWED_HOSTS = ["*"]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)
