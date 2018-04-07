from django.utils.translation import ugettext_lazy as _

# number_regex = {
#     'pattern': '^(\d{,5})([a-zA-Z]?)(/?)\d{,5}[^/]$', 'message': _('Pole zawiera niedozwolone znaki.')}
forbidden_chars_regex = {
    'pattern': '^[^<>\'!@`~\"]+$', 'message': _('Pole zawiera niedozwolone znaki.')}

pattern = forbidden_chars_regex['pattern']
message = forbidden_chars_regex['message']
