
import pytest
from django.db import connection


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        cur = connection.cursor()
        cur.execute("UPDATE django_site SET domain='127.0.0.1:8000' WHERE id=2;")