from django.db import models
from scribe.includes.districts import districts
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from .includes.regexes import number_regex, street_regex
import datetime


class TransitRouteModel(models.Model):

    # TODO: add default = request.user.default_street
    origin_street = models.CharField(
        max_length=40, default='Walecznych', validators=[RegexValidator(regex=street_regex['pattern'], message=street_regex['message'])])
    # TODO: add default = request.user.default_city
    origin_city = models.CharField(max_length=40, default='Klodzko')
    # TODO: add default = request.user.default_district
    origin_district = models.CharField(
        max_length=30, choices=districts, null=True, default='districts.dol')

    destination_street = models.CharField(max_length=40, default='Hallera', validators=[RegexValidator(regex=street_regex['pattern'], message=street_regex['message'])])
    destination_city = models.CharField(max_length=40, default='Wroclaw')
    destination_district = models.CharField(
        max_length=30, choices=districts, null=True, default='districts.dol')

    paycheck_for_route = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    # TODO: take it from userprofile, change after add user module
    pln_per_km = models.DecimalField(
        max_digits=6, decimal_places=2, default=2.5)

    distance_in_km = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    # TODO: add datetime.date.today()
    transit_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.origin_city + ' - ' + self.destination_city + ' ' + self.transit_date.strftime('%d-%m-%Y')

 # TODO: add disctance field saved after get response from google maps api
