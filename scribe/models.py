from django.db import models
from scribe.includes.districts import districts
import datetime


class TransitRouteModel(models.Model):

    # TODO: add default = request.user.default_no
    source_adress_number = models.CharField(max_length=40)
    # TODO: add default = request.user.default_street
    source_adress_street = models.CharField(max_length=40)
    # TODO: add default = request.user.default_city
    source_adress_city = models.CharField(max_length=40)
    # TODO: add default = request.user.default_district
    source_adress_district = models.CharField(
        max_length=30, choices=districts, null=True)

    endpoint_adress_number = models.CharField(max_length=40)
    endpoint_adress_street = models.CharField(max_length=40)
    endpoint_adress_city = models.CharField(max_length=40)
    endpoint_adress_district = models.CharField(
        max_length=30, choices=districts, null=True)

    # TODO: add datetime.date.today()
    transit_date = models.DateField(auto_now_add=True)
