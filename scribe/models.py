from django.db import models
from scribe.includes.districts import districts
from django.utils import timezone

import datetime


class TransitRouteModel(models.Model):

    # TODO: add default = request.user.default_no
    source_adress_number = models.CharField(
        max_length=40, default=' ')
    # TODO: add default = request.user.default_street
    source_adress_street = models.CharField(max_length=40)
    # TODO: add default = request.user.default_city
    source_adress_city = models.CharField(max_length=40)
    # TODO: add default = request.user.default_district
    source_adress_district = models.CharField(
        max_length=30, choices=districts, null=True)

    endpoint_adress_number = models.CharField(
        max_length=40, null=True, blank=True)
    endpoint_adress_street = models.CharField(max_length=40)
    endpoint_adress_city = models.CharField(max_length=40)
    endpoint_adress_district = models.CharField(
        max_length=30, choices=districts, null=True)

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
        return self.source_adress_city + self.endpoint_adress_city + self.transit_date

 # TODO: add disctance field saved after get response from google maps api
