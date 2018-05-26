
import pytest
from django.db import connection


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        cur = connection.cursor()
        cur.execute("UPDATE django_site SET domain='127.0.0.1:8000' WHERE id=2;")
        cur.execute("INSERT INTO `user_login_register_app_user`(`id`,`password`,`last_login`,`email`,`username`,`active`,`staff`,`admin`) VALUES (99,'bumerang','2018-05-24 19:14:47.149315','testuser99@gmail.com','testuser99','True','False','False');")


        