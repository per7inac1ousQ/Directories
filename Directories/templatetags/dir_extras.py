from django import template
from django.db import models
from django.db.models import get_models, get_app, get_model
from Directories.models import Department, Attributes
register = template.Library()

@register.filter
def upper(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.upper()

'''
def dlist(request):
		print "field_list: ", z
		count = 0
		field_counter = 0
		for f_name in field_names:	
			for mod in model_list:
				j = getattr(mod, field_list[count])		
				c.append(f_name)	
				k.append(j)	
			count += 1
	y = zip(c,k)
	asa = ''.join(column.rjust(10) for column in str(k))
'''

@register.inclusion_tag('Directories/model_data.html')
def model_data_table(name):
	model_class = get_model('Directories', name)
	#Returns model data in table form
	for field in model_class._meta.get_all_field_names():
		data_list = model_class.objects.all()
	return {'data_list':data_list}
	#for f_name in model._meta.get_all_field_names():
	#data_list = model_class.objects.all()#select_related(f_name)
	
#	return "hello"


@register.inclusion_tag('Directories/model_data.html')
def field_data(field):
	#model_list = model_class.objects.all() 
	#initialise fields and their names
	#fields = model_class._meta.fields
	#field_names = model_class._meta.get_all_field_names()
	#s_field = model._meta.get_field(field).verbose_name	
	data_list = Attributes.objects.values_list(field, flat=True)
	#if s_field:		
		#for mod in model.objects.all():		
	return {'data_list':data_list}
	#j = model.objects.all()
	#return "hello"
    #return getattr(model, field)	


######## Ways to get specific field and/or its values #####################
# 1) model._meta.get_field(field)
# 2) model.objects.values(s_field)
# 3) model.objects.values_list(s_field)
# 4) getattr(model, field)



