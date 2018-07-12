
import pytest
from django.db import connection
import datetime


today = str(datetime.date.today())



@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        cur = connection.cursor()
        cur.execute("UPDATE django_site SET domain='127.0.0.1:8000' WHERE id=2;")
        cur.execute("INSERT INTO `user_login_register_app_user`(`id`,`password`,`last_login`,`email`,`username`,`active`,`staff`,`admin`) \
        												VALUES (99,'bumerang','2018-05-24 19:14:47.149315','testuser99@gmail.com','testuser99','True','False','False');")
        cur.execute("INSERT INTO `user_login_register_app_profile`(`id`,`email_confirmed`,`user_cretion_date`,`user_id`,`user_pln_per_km`) \
        													VALUES (99,1,'2018-05-24 00:00:00',99,2);")
        cur.execute("INSERT INTO `scribe_transitroutemodel`(`id`,`user_instance_id`,`origin_street`,`origin_city`,`origin_district`,`destination_street`,\
        	`destination_city`,`destination_district`,`paycheck_for_route`,`distance_in_km`,`transit_date`) \
        	VALUES (1,99,'Walecznych 59','Kłodzko','Dolnośląskie','Petuniowa 9','Wrocław','Dolnośląskie',176.8,88.4,'2018-05-01');")
        cur.execute("INSERT INTO `scribe_transitroutemodel`(`id`,`user_instance_id`,`origin_street`,`origin_city`,`origin_district`,`destination_street`,\
        	`destination_city`,`destination_district`,`paycheck_for_route`,`distance_in_km`,`transit_date`) \
        	VALUES (2,99,'Walecznych 59','Kłodzko','Dolnośląskie','Wiejska 4','Warszawa','Mazowieckie',900,450," + today + ");")


@pytest.fixture()
def client():
    """A Django test client instance."""
    skip_if_no_django()

    from django.test.client import Client

    return Client()


@pytest.fixture()
def django_user_model(db):
    """The class of Django's user model."""
    from django.contrib.auth import get_user_model
    return get_user_model()


@pytest.fixture()
def django_username_field(django_user_model):
    """The fieldname for the username used with Django's user model."""
    return django_user_model.email # Balouscange for real USERNAME_FIELD


@pytest.fixture()
def admin_user(db, django_user_model, django_username_field):
    """A Django admin user.

    This uses an existing user with username "admin", or creates a new one with
    password "password".
    """
    UserModel = django_user_model
    username_field = django_username_field

    try:

        user = UserModel._default_manager.get(**{username_field: 'admin'})
    except UserModel.DoesNotExist:
        extra_fields = {}
        if username_field != 'username':
            extra_fields[username_field] = 'admin'
        user = UserModel._default_manager.create_superuser(
            'admin', 'admin@example.com', 'password', **extra_fields)
    return user


@pytest.fixture()
def admin_client(db, admin_user):
    """A Django test client logged in as an admin user."""
    from django.test.client import Client

    client = Client()
    client.login(username=admin_user.username, password='password')
    return client


@pytest.fixture()
def django_user(db, django_user_model, django_username_field):
    """A Django user.
    This uses an existing user with username "user", or creates a new one with
    password "password".
    """
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(email='testuser@gmail.com')			#(**{username_field: 'user'})
    except UserModel.DoesNotExist:
        #extra_fields = {}
        #if username_field != 'username':
            #extra_fields[username_field] = 'user'
        user = UserModel._default_manager.create_user(
            'testuser@gmail.com', 'testuser', 'bumerang', is_active=True)#**extra_fields)
    return user


@pytest.fixture()
def user_client(db, django_user):
    """A Django test client logged in as a normal user."""
    from django.test.client import Client

    client = Client()
    client.login(username=django_user.email, password='bumerang')#(username=django_user.username, password='password')
    return client


       
