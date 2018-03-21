from django.forms import ModelForm
from .models import TransitRouteModel
import datetime
from django import forms


class TransitRouteForm(forms.ModelForm):
        # TODO: merge this with html input type='data'
    filter_date_from = forms.DateField(initial=datetime.date.today)
    filter_date_to = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = TransitRouteModel
        fields = ('source_adress_number', 'source_adress_street',
                  'source_adress_city', 'source_adress_district',
                  'endpoint_adress_number', 'endpoint_adress_street',
                  'endpoint_adress_city', 'endpoint_adress_district',
                  'filter_date_from', 'filter_date_to', )
