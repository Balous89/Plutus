from django.forms import ModelForm
from .models import TransitRouteModel
from django.utils.translation import ugettext_lazy as _
import datetime
from django import forms
import datetime

# TODO: merge this with html input type='data'


class TransitRouteForm(forms.ModelForm):
  
  origin_number = forms.CharField(max_length=40,label=_('Numer'))
  destination_number = forms.CharField(max_length=40,label=_('Numer'))

  class Meta:
    model = TransitRouteModel
    fields = ('origin_number', 'origin_street', 'origin_city', 
              'origin_district', 'destination_number',
              'destination_street', 'destination_city', 
              'destination_district',
              )
    labels = {
        'origin_street': _('Ulica'),
        'origin_city': _('Miasto'),
        'origin_district': _('Województwo'),
        'destination_street': _('Ulica'),
        'destination_city': _('Miasto'),
        'destination_district': _('Województwo'),
    }

class DateFilterForm(forms.Form):
  today = datetime.date.today().strftime('%Y-%m-%d')

  date_from = forms.DateField(widget=forms.widgets.DateInput(format="%Y-%m-%d"),
                              error_messages={'invalid':_('Wprowadź datę w formacie ' + today)},
                              label=_('Data od:'))
  date_to = forms.DateField(widget=forms.widgets.DateInput(format="%Y-%m-%d"),
                            error_messages={'invalid':_('Wprowadź datę w formacie ' + today)},
                            label=_('Data do:'))
