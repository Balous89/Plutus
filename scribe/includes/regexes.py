from django.utils.translation import ugettext_lazy as _
number_regex = {
    'pattern': '^(\d{,5})([a-zA-Z]?)(/?)\d{,5}[^/]$', 'message': _('Please enter valid number')}
street_regex = {
    'pattern': '^[^<>\'!@`~]+$', 'message': _('Please enter valid streetname')}

