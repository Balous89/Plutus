from django.forms import ModelForm
from .models import TransitRouteModel
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms
from django.core.validators import RegexValidator
from .includes.regexes import number_regex, street_regex
import re

# TODO: merge this with html input type='data'

class TransitRouteForm(forms.ModelForm):
  
  origin_number = forms.CharField(max_length=40,label=_('Numer'))
  destination_number = forms.CharField(max_length=40,label=_('Numer'))

  class Meta:
    model = TransitRouteModel
    fields = ('origin_number', 'origin_street', 'origin_city', 'origin_district', 'destination_number',
              'destination_street', 'destination_city', 'destination_district',
              )
    labels = {
        'origin_street': _('Ulica'),
        'origin_city': _('Miasto'),
        'origin_district': _('Województwo'),
        'destination_street': _('Ulica'),
        'destination_city': _('Miasto'),
        'destination_district': _('Województwo'),
    }
