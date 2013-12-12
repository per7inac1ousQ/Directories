from django import template
from django.db import models
from django.db.models import get_models, get_app, get_model
from Directories.models import Department, Attributes
register = template.Library()

@register.filter
def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()


#@register.filter
#def field_name(model, field_value):
	#model.objects.get(field_value)
	# get_field_d = model_class.objects.values_list(f_name)
	#for k in model.objects.values_list(field_value):
	#	return k
	#my_filter = {}
	#my_filter[my_keyword] = filter_value
	#my_model = model.objects.filter(**my_filter)
	#returns the field 
	#model.__getitem__ = field_value
	#return model[field_value]
'''
if not field_list:
		z = create_field_list(model_class)#[count]
		print "field_list: ", z
		count = 0
		field_counter = 0
		for f_name in field_names:	
			for mod in model_list:
				j = getattr(mod, field_list[count])	
				#strj = '<td> %s </td>' %j		
				c.append(f_name)	
				#k.append(strj)				
				k.append(j)
				
				#j = j.encode('ISO 8859-7')
				#j = j.encode('windows-1253').decode('utf-8')
			count += 1
'''
@register.inclusion_tag('Directories/model_data.html')
def model_data_table():
	#Returns model data in table form
	#for f_name in model._meta.get_all_field_names():
	data_list = Attributes.objects.all()#select_related(f_name)
	return {'data_list':data_list}
#	return "hello"

