from django.forms import ModelForm
from .models import TransitRouteModel
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms
import re


class TransitRouteForm(forms.ModelForm):
        # TODO: merge this with html input type='data'
  class Meta:
    model = TransitRouteModel
    fields = ('source_adress_number', 'source_adress_street',
              'source_adress_city', 'source_adress_district',
              'endpoint_adress_number', 'endpoint_adress_street',
              'endpoint_adress_city', 'endpoint_adress_district',
              )
    widgets = {
        'source_adress_number': forms.TextInput(attrs={'placeholder': 'To pole nie jest wymagane'}),
        'endpoint_adress_number': forms.TextInput(
            attrs={'placeholder': 'To pole nie jest wymagane'}),
    }
    labels = {
        'source_adress_number': _('Numer'),
        'source_adress_street': _('Ulica'),
        'source_adress_city': _('Miasto'),
        'source_adress_district': _('Województwo'),
        'endpoint_adress_number': _('Numer'),
        'endpoint_adress_street': _('Ulica'),
        'endpoint_adress_city': _('Miasto'),
        'endpoint_adress_district': _('Województwo'),
    }

  def clean_source_adress_number(self):
    source_adress_number = self.cleaned_data.get('source_adress_number')
    number_pattern = re.compile(r'^(\d{,5})([a-zA-Z]?)(/?)\d{,5}$')
    if (bool(number_pattern.match(source_adress_number)) is False) or source_adress_number[-1] == '/':
      raise forms.ValidationError(_('Please enter valid number'))
    return source_adress_number

  def clean_endpoint_adress_number(self):
    endpoint_adress_number = self.cleaned_data.get('endpoint_adress_number')
    number_pattern = re.compile(r'^(\d{,5})([a-zA-Z]?)(/?)\d{,5}$')
    if (bool(number_pattern.match(endpoint_adress_number)) is False) or endpoint_adress_number[-1] == '/':
      raise forms.ValidationError(_('Please enter valid number'))
    return endpoint_adress_number
