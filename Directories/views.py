import re
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

model_classes = []
data = []
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
			'model_object': model.objects.all()  
		})
	return model_classes

def index(request):
	model_classes = models()
	model_form = dbForm()
	print "NOOOTTTTTTTTTTTTTTTTTTTTTT VALIDDDDDDDDDDDDDD FORM!"
	if request.method == 'POST':
		model_form = dbForm(request.POST)
		if model_form.is_valid():
			print "FORM VALIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDDDDD!"			
			model_classes_field  = model_form.cleaned_data['model_classes_field']
			return render(request, 'Directories/index.html', {'model_classes':model_classes})	
	return render(request, 'Directories/index.html', {'model_form':model_form, 'model_classes':model_classes
})

def get_model_fields(model):
	return model._meta.fields

def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def dlist(request):
 
	#get the model id selected in the POST form and convert it to an integer
	m_tb_name= request.POST['model_classes_field']
	model_class = get_model('Directories', m_tb_name)
	#data = serializers.serialize("xml"  model_class.objects.all())
	model_list = model_class.objects.all() # find why it returns "objects" and
											# no values. Elusa kati paromoio
 # sto django tutorial
	#print model_objs(model_class)
# how the data will be handled in list.html
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()

	#for f_name in model_class._meta.fields:
		#print "data is data: ", str(f_name) 
	for f_name in field_names:	
		mlist = model_class.objects.filter(f_name = descr)

	for mod in model_list:
		#print "mod: ", mod
		#mod.split(',')
		for f_name in field_names:		
			#data = getattr(mod, f_name)
			data = "douf"
			text = re.split(',', str(mod))
			print "TEXTTT! : ", text
			#print re.split(',', str(mod))
#print "damn: ", dir(model_class)	# otan teleiwseis svisto...	

#	print dep_field[0].rel
#dep_field[0].rel.field_name
#dep_field[0].rel.to
######################################################3
	#print 'You searched for: %r' % m_tb_name
	return render(request, 'Directories/list.html', {'m_tb_name':m_tb_name, 'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'data':data})

#def get_mod_field(model, field_name):
#	return model._meta.get_field(field_name)

class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models())	

	#def __init__(self, *args, **kwargs):
 #       super(dbForm, self).__init__(*args, **kwargs)
  #      self.fields['model_classes_field'].choices = [(x.pk, x.get_full_name()) for x in User.objects.all()]

def get_data(model):
	for mod in model.objects.all():
		#print "mod: ", mod
		for f_name in model._meta.get_all_field_names():
			#print mod.get_mod_field(mod, f_name)
			data.append ({ getattr(mod, f_name) })
			#print "f_name is ", f_name
	return data

######## kane mia me8odo gia na kaneis append()
####### ta objects kai na ta emfanizeis se morfi mod.f
###### dioti etsi opws einai dn ta anagnwrizei.
def model_fields(model):
	field_names = model._meta.get_all_field_names()
	for field in field_names:
		f_names.append({ 
			'field_name': field
	})
	return f_names

def model_objs(model):
	model_list = model.objects.all()
	#print model_list
	for obj in model_list:
		#obj.append({ 
			obj
	#})
	
	return obj
######################################


