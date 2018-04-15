from django.db import models
from scribe.includes.districts import districts
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from .includes.regexes import forbidden_chars_pattern, forbidden_chars_message
from user_login_register_app.models import Profile
from django.contrib.auth import get_user_model

import datetime

User = get_user_model()


class TransitRouteModel(models.Model):

    user_instance = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    # TODO: add default = request.user.default_street
    origin_street = models.CharField(max_length=40,
                                     validators=[RegexValidator(
                                        regex=forbidden_chars_pattern, 
                                        message=forbidden_chars_message)],
                                     default='')
    # TODO: add default = request.user.default_city
    origin_city = models.CharField(max_length=40, validators=[RegexValidator(
                                        regex=forbidden_chars_pattern, 
                                        message=forbidden_chars_message)],
                                    )
    # TODO: add default = request.user.default_district
    origin_district = models.CharField(max_length=30,
                                       choices=districts, null=True,
                                       validators=[RegexValidator(
                                           regex=forbidden_chars_pattern, 
                                           message=forbidden_chars_message)],
                                       default='districts.dol')

    destination_street = models.CharField(max_length=40,
                                          validators=[RegexValidator(
                                            regex=forbidden_chars_pattern, 
                                            message=forbidden_chars_message)], 
                                          default='Hallera', )
    destination_city = models.CharField(max_length=40, validators=[
                                        RegexValidator(
                                            regex=forbidden_chars_pattern, 
                                            message=forbidden_chars_message)], 
                                        default='Wroclaw')
    
    destination_district = models.CharField(max_length=30, choices=districts, 
                                            null=True, validators=[RegexValidator(
                                                regex=forbidden_chars_pattern, 
                                                message=forbidden_chars_message)], 
                                            default='districts.dol')

    paycheck_for_route = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    # TODO: take it from userprofile, change after add user module
    # pln_per_km = models.DecimalField(max_digits=6, decimal_places=2, default=2.5) # TODO REMOVE??

    distance_in_km = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # TODO: add datetime.date.today()
    transit_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.origin_city + ' - ' + self.destination_city + ' ' + self.transit_date.strftime('%d-%m-%Y')

    def get_paycheck_for_route(self):
        return self.paycheck_for_route

 # TODO: add disctance field saved after get response from google maps api
