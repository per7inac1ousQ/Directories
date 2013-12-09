from django import template
from django.db import models

register = template.Library()

@register.filter
def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()


@register.filter
def field_name(model, field_value):
	for f_name in model._meta.get_all_field_names():
		my_filter[my_keyword] = field_value
	#my_filter = {}
	#my_filter[my_keyword] = filter_value
	#my_model = model.objects.filter(**my_filter)
	#returns the field 
	model.__getitem__ = field_value
	return model[field_value]

