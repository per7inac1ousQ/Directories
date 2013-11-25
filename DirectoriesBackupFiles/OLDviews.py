from django import forms
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

# function that iterates through all of the models in the database and 
# returns their name and position
def models():
	apps = get_app('Directories')
	m_id = 0
	for model in get_models(apps):
		m_id += 1
		model_classes.append({
			'model_name': model._meta.verbose_name,
			'model_id': m_id
			#'model_table': model._meta.db_table,  ----display each table of the db
			#'model_object': model.objects.all()   ----display all objects
		})
	return model_classes

def get_name(m_id):
	apps = get_app('Directories')
	model_id = 0
	for model in get_models(apps):
		model_id += 1
		if (m_id == model_id):
			name = model._meta.verbose_name
			model_id = m_id
			break
		print model_id
	return name

def index(request):
	model_classes = models()
	#m_id = 8585
	model_form = dbForm()
	#request.session['model_classes_field'] = mchoices
	print "NOOOTTTTTTTTTTTTTTTTTTTTTT VALIDDDDDDDDDDDDDD FORM!"
	if request.method == 'POST':
		model_form = dbForm(request.POST)
		if model_form.is_valid():
			print "FORM VALIIIIIIIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDDDDD!"			
			model_classes_field  = model_form.cleaned_data['model_classes_field']
			return render(request, 'Directories/index.html', {'model_classes':model_classes})	
	return render(request, 'Directories/index.html', {'model_form':model_form, 'model_classes':model_classes
})

#def get_model_fields(model):
#	return model._meta.fields

def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def dlist(request):
	#get the model id selected in the POST form and convert it to an integer
#	m_id= int(request.POST['model_classes_field'])
	m_name= request.POST['model_classes_field']
	model_class = get_model('Directories', m_name)
	print "problematic table:"
	print model_class	
#	print get_name(m_id)
#	model_list = model_class.objects.all()
###################################################
# how the data will be handled in list.html
#model = models.get_model('timeapp', 'Employee')
#	dep_field = model_class._meta.get_field_by_name('attr_id')
#	print dep_field
#dep_field[0].rel.field_name
#Out[4]: 'id'
#In [5]: 
#dep_field[0].rel.to
#Out[5]: <class 'timesite.timeapp.models.Department'>
######################################################3
	print 'You searched for: %r' % m_name
	#model_classes.model_id=pos
	#print model_classes.model_id
# take the position of model chosen in the index through POST
# and populate the tables....
#	return render(request, 'Directories/list.html', {'m_id':m_id, 'model_class':model_class})
	return render(request, 'Directories/list.html', {'m_name':m_name, 'model_class':model_class})

class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models())



