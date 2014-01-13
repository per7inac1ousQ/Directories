from django import template
from django.db import models
from django.db.models import get_models, get_app, get_model
from Directories.models import Department, Attributes
register = template.Library()

@register.filter
def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()

@register.filter
def field_values():
	#data = model.objects.values_list(field, flat=True)
	#data_list = list(data)
   return Attributes.objects.values_list("attr_id", flat=True)

@register.assignment_tag
def get_random_testimonial():
   return Attributes.objects.order_by('?')[0]

#@register.assignment_tag
#def get_random_testimonial(field):
#	return Attributes.objects.values_list(field, flat=True)

@register.inclusion_tag('Directories/model_data.html')
def field_data(field):
	#model_list = model_class.objects.all() 
	#initialise fields and their names
	#fields = model_class._meta.fields
	#field_names = model_class._meta.get_all_field_names()
	#s_field = model._meta.get_field(field).verbose_name	
	data_list = Attributes.objects.values_list(field, flat=True)
	#data_list = Attributes.objects.get(id).values_list()		
	return {'data_list':data_list}


######## Ways to get specific field and/or its values #####################
# 1) model._meta.get_field(field)
# 2) model.objects.values(s_field)
# 3) model.objects.values_list(s_field)
# 4) getattr(model, field)



