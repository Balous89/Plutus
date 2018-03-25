from django.forms import ModelForm
from .models import TransitRouteModel
from django.utils.translation import ugettext_lazy as _
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
    widgets = {
        'source_adress_number': forms.TextInput(attrs={'placeholder': 'To pole nie jest wymagane'}),
        'endpoint_adress_number': forms.Textarea(
            attrs={'placeholder': 'To pole nie jest wymagane'}),
    }
    labels = {
        'source_adress_number': _('Numer'),
        'source_adress_street': _('Ulica'),
        'source_adress_city': _('Miasto'),
        'source_adress_district': _('Województwo'),
    }

 # source_adress_number = models.CharField(
 #        max_length=40, label=_('Numer'), required=False, )
 #    # TODO: add default = request.user.default_street
 #    source_adress_street = models.CharField(max_length=40, label=_('Ulica'))
 #    # TODO: add default = request.user.default_city
 #    source_adress_city = models.CharField(max_length=40, label=_('Miasto'))
 #    # TODO: add default = request.user.default_district
 #    source_adress_district = models.CharField(
 #        max_length=30, choices=districts, null=True, label=_('Województwo'))

 #    endpoint_adress_number = models.CharField(max_length=40, label=_('Numer'))
 #    endpoint_adress_street = models.CharField(max_length=40, label=_('Ulica'))
 #    endpoint_adress_city = models.CharField(max_length=40, label=_('Miasto'))
 #    endpoint_adress_district = models.CharField(
 #        max_length=30, choices=districts, null=True, label=_('Województwo'))
