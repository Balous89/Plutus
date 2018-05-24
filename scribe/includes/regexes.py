from django.utils.translation import ugettext_lazy as _

forbidden_chars_regex = {
    'pattern': '^[^<>\'!@`~\"()]+$', 'message': _('Field contains illegal characters.')}

forbidden_chars_pattern = forbidden_chars_regex['pattern']
forbidden_chars_message = forbidden_chars_regex['message']
