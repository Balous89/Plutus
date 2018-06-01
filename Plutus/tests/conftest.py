
import pytest
from django.db import connection


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        cur = connection.cursor()
        cur.execute("UPDATE django_site SET domain='127.0.0.1:8000' WHERE id=2;")
        cur.execute("INSERT INTO `user_login_register_app_user`(`id`,`password`,`last_login`,`email`,`username`,`active`,`staff`,`admin`) VALUES (99,'bumerang','2018-05-24 19:14:47.149315','testuser99@gmail.com','testuser99','True','False','False');")
        cur.execute("INSERT INTO `user_login_register_app_profile`(`id`,`email_confirmed`,`user_cretion_date`,`user_id`,`user_pln_per_km`) VALUES (99,1,'2018-05-24 00:00:00',99,2);")

        #cur.execute("INSERT INTO `user_login_register_app_user`(`id`,`password`,`last_login`,`email`,`username`,`active`,`staff`,`admin`) VALUES (99,'bumerang','2018-05-24 19:14:47.149315','testuser@gmail.com','testuser','True','False','False');")
        #cur.execute("INSERT INTO `scribe_transitroutemodel`(`id`,`user_instance_id`,`origin_street`,`origin_city`,`origin_district`,`destination_street`,`destination_city`,`destination_district`,`paycheck_for_route`,`distance_in_km`,`transit_date`) VALUES (1,99,'Testowa 1','Testowo Wielkie','Dolnośląskie','Testowa 99','Testowo Wielkie','Dolnośląskie','200.0','100.0','2018-05-28');")
















# import pytest
# from django.db import connection


# @pytest.fixture(scope='session')
# def django_db_setup(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         cur = connection.cursor()
#         cur.execute("UPDATE django_site SET domain='127.0.0.1:8000' WHERE id=2;")
#         cur.execute("INSERT INTO `user_login_register_app_user`(`id`,`password`,`last_login`,`email`,`username`,`active`,`staff`,`admin`) VALUES (99,'bumerang','2018-05-24 19:14:47.149315','testuser99@gmail.com','testuser99','True','False','False');")


#         