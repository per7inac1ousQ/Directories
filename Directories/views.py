from django import forms
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import loader, RequestContext
from django.db import models
from django.db.models import get_models, get_app, get_model
from Directories.models import Department, Attributes
from django.shortcuts import render, get_object_or_404
from django.utils.http import base36_to_int
from django.core.paginator import Paginator

model_classes = []
field_list = []
k = []
c = []
# function that iterates through all of the models in the database and 
# returns their name and position
def models():
	apps = get_app('Directories')
	m_id = 0
	for model in get_models(apps):
		m_id += 1
		model_classes.append({
			'model_name': model._meta.verbose_name,
			'model_id': m_id,
			'model_table': model._meta.db_table,
			#'model_objects': model.objects.all()  
		})
		#print model.objects.all()
	return model_classes

def models2(model):
	apps = get_app('Directories')
	for model in get_models(apps):
		model_data = model.objects.all()
	return model_data

def index(request):
	if request.method == 'POST': # If the form has been submitted...
		form = dbForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			model_classes_field = form.cleaned_data['model_classes_field']
			return HttpResponseRedirect('/list/') # Redirect after POST
		else:
			print "form: ", form.errors
	else:
		form = dbForm() # An unbound form
		print "form: ", form.errors
		print "not valiiiid form"

	return render(request, 'Directories/index.html', {
		'form': form,
	})

def get_model_fields(model):
	return model._meta.fields

def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def dlist(request):
	#get the model id selected in the POST form and convert it to an integer
	m_tb_name= request.POST['model_classes_field']
	print 'You searched for: %r' % m_tb_name
	model_class = get_model('Directories', m_tb_name)
	model_list = model_class.objects.all() 
	#initialise fields and their names
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()
#print "damn: ", dir(model_class)	# otan teleiwseis svisto...	
	#count = 0
	
	#for field in model_class._meta.fields: 
	#	print "model field is: ", model_class.get_field(field)
	
	if not field_list:
		z = create_field_list(model_class)#[count]
		print "field_list: ", z
		count = 0
		field_counter = 0
		#d = model_class.objects.filter(**{z})
		for f_name in field_names:	
			#k = model_class.objects.filter(f_name)
			#if f_name == 'attr_id':
				#print "YES!"
			
			#c.append(f_name)	
			for mod in model_list:
				#j = getattr(mod, "descr")
				#j = getattr(mod, get_field_list(model_class)[0])
				j = getattr(mod, field_list[count])			
				#j = j.encode('ISO 8859-7')	
				c.append(f_name)	
				k.append(j)
				#n = zip(str(f_name), str(mod))
				#k[count].append(j)	
				#d = model_class.objects.filter(*{k})
				#print "j is: ", j 
				#j = j.encode('utf-8') # WORKS for english charsnmy
				#j = j.encode('latin-1') # NOT working...
				#j = j.encode('ISO 8859-7') # greek is 'ISO 8859-7' or'windows-1253'
				#j = j.encode('windows-1253')
				#j = j.encode('windows-1253').decode('utf-8')
				#j = j.encode('ISO 8859-7').decode('ascii') 
			#print "field list is: ", field_list[count]
			count += 1
#b = model_class.object.filter(?????)
	#elif field_list != []:
	#	z = remove_field_list(model_class)
	#	print "EMPTY?? ", field_list
	z = remove_field_list(model_class)
	#print "objects inside list? ", len(field_list)
	#print "field is: ", j
	#j="j"
	#k = [(field_list, model_list)]
	#print 'You searched for: %r' % m_tb_name
	y = zip(c,k)
	first_elem = [i[0] for i in y]
	#pagination(model_list, 25) ####################################???????
	return render(request, 'Directories/list.html', {'m_tb_name':m_tb_name, 'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'k':k, 'c':c, 'y':y, 'first_elem': first_elem})

#def get_mod_field(model, field_name):
#	return model._meta.get_field(field_name)

#returns a list of field names
def create_field_list(model):
	print "list create "
	for f_name in model._meta.get_all_field_names():
		#print "field name is: ", f_name
		field_list.append(f_name)
	return field_list

def remove_field_list(model):
	print "list delete "	
	for f_name in model._meta.get_all_field_names():
		#print "field name is: ", f_name
		field_list.remove(f_name)
	return field_list

'''
def encode_check(text):
	if text.encodingtype == 'utf-8'.........
'''

class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models(), required=True,)	

	#def __init__(self, *args, **kwargs):
 #       super(dbForm, self).__init__(*args, **kwargs)
  #      self.fields['model_classes_field'].choices = [(x.pk, x.get_full_name()) for x in User.objects.all()]

'''
class modelForm(forms.Form):
	model_classes_field = forms.ModelChoiceField(queryset = Attributes.objects.all())	

	def __init__(self, *args, **kwargs):
		super(modelForm, self).__init__(*args, **kwargs)
		self.fields['model_classes_field'].queryset = Attributes.objects.all()
'''




