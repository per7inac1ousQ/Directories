from django import temlpate
from datetime import date, timedelta

register = template.Library()

@register.filter
def to_class_name(value):
	return value.__class__.__name__
