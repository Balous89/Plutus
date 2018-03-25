from django import template


register = template.Library()


@register.filter(name='source_form_fields')
def source_form_fields(value):
    if value.name in ('source_adress_number', 'source_adress_street',
                      'source_adress_city', 'source_adress_district'):
        return value
    else:
        return ('')


@register.filter(name='label_form_fields')
def label_form_fields(value):
    if value.name in ('source_adress_number', 'source_adress_street',
                      'source_adress_city', 'source_adress_district'):
        return value.label
    else:
        return ('')


@register.simple_tag
def endpoint_form_fields(value):
    if value.name in ('endpoint_adress_number', 'endpoint_adress_street',
                      'endpoint_adress_city', 'endpoint_adress_district'):
        return value
    else:
        return ('')
