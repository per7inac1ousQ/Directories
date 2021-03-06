from django import template
from django.db import models
from django.db.models import get_models, get_app, get_model
from Directories.models import Department, Attributes
from django.template import loader, RequestContext
register = template.Library()

data_list = []
result_list = []

@register.filter(name='field_values')
def field_values(model, field):
   model_class = get_model('Directories', model) 
   return list(model_class.objects.values_list(field, flat=True))

@register.simple_tag
def get_value_from_key(object, key):
	return object[key.name]
'''
@register.assignment_tag()
def resolve(lookup, target):
    try:
        return Variable(lookup).resolve(target)
    except VariableDoesNotExist:
        return None
  '''      
#@register.assignment_tag
#def get_random_testimonial(field):
#	return Attributes.objects.values_list(field, flat=True)

#@register.inclusion_tag('Directories/model_data.html')
#def model_data_table(name):
#	model_class = get_model('Directories', name)
	#Returns model data in table form
#	for field in model_class._meta.get_all_field_names():
#		data_list = model_class.objects.all()
#	return {'data_list':data_list}
	#for f_name in model._meta.get_all_field_names():
	#data_list = model_class.objects.all()#select_related(f_name)
	
#	return "hello"

@register.inclusion_tag('Directories/model_data.html')
def field_data(model, field):
	model_class = get_model('Directories', model)
	fields_lst= list(model_class.objects.values_list(field, flat=True)) 		
	return {'fields_lst':fields_lst}
'''
@register.inclusion_tag('Directories/field_edit.html')
def field_edit(model, field):	
	if request.method == 'POST':
		print "SLECTEDDDDDDDDDDDD SAYIN!"
		print "YEAHHHH!"
		#form_class = get_fields_dynamic (request.GET['model_classes_field'])
		#form = form_class(request.POST)
		sForm = selectForm(request.POST)
		if sForm.is_valid(): # All validation rules pass
			print "YEAHHHH!"
		return render(request, 'Directories/index.html', {'form':form}) # form or sForm??
'''
@register.inclusion_tag('Directories/field_edit.html')
def field_edit(model, field):
	model_class = get_model('Directories', model)
	fields_lst= list(model_class.objects.values_list(field, flat=True))
	return {'fields_lst':fields_lst}

'''
@register.inclusion_tag('Directories/model_data.html')
def field_data(model, field):
	model_class = get_model('Directories', model)
	data_list = model_class.objects.values_list(field, flat=True)
	#data_list = Attributes.objects.get(id).values_list()		
	return {'data_list':data_list}
'''

######## Ways to get specific field and/or its values #####################
# 1) model._meta.get_field(field)
# 2) model.objects.values(s_field)
# 3) model.objects.values_list(s_field)
# 4) getattr(model, field)



