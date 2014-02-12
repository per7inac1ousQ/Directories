import datetime
import itertools
import collections
from Directories.forms import dbForm, editForm, get_dynamic_form, selectForm, selectForm2, get_fields_dynamic
from Directories.models import Department, Attributes, Employees, Instructors, Katefth, KatefthKykloi, Kykloi, KykloiExamina, ModuleKykloi, Modules, ModulesTutors, PubInstr, PubTypes, Publications, Ranks, Service, Users, Works
from django import forms
from django.core import serializers
from django.db.models import get_models, get_app, get_model
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import loader, RequestContext
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Template
from django.core.paginator import Paginator
from django.http import Http404
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms import Textarea
from django.contrib import messages
#import django_tables as tables 

model_classes = []
field_choices = []
fields_dict = []
field_list = []
field_models = []
field_values = {}
k = []
c = []
update_list = []

def fields(model, field):
	m_values = model.objects.values_list(field, flat=True) # field = field_list[2]
	for val in m_values:
		field_choices.append( (val, val), )
	return field_choices
	
def index(request): #for two submit buttons:
	print "start"
	#print fields()
	form = dbForm()
	if request.method == 'GET':	
		print "get!!!"
		if '_change' in request.GET:
			form = dbForm(request.GET) 
			print "i am in _change submit button"
			if form.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = form.cleaned_data['model_classes_field']	
				return HttpResponseRedirect(reverse('Directories:list_models'))		
				#return render(request, 'Directories/list.html', {'model_classes_field':model_classes_field})
			else:
				return HttpResponse('ERROR in GET -- Return to form submission')
		elif '_add' in request.GET:
			form = dbForm(request.GET)
			print "i am in _add submit button"
			if form.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = form.cleaned_data['model_classes_field']	
				return HttpResponseRedirect(reverse('Directories:update_directories'))	
				#return render(request, 'Directories/create.html', {'model_classes_field':model_classes_field})
			else:
				return HttpResponse('ERROR in GET -- Return to form submission')
	else:
		form = dbForm()
		print "no POST - form: ", form.errors
		print "unbound form"
 	return render(request, 'Directories/index.html', {'form':form})

'''
	View that displays a list of all model objects
'''
def dlist(request):
	print "list page"
	m_tb_name = request.GET['model_classes_field'] # get the model table name
	model_class = get_model('Directories', m_tb_name)
	model_name = model_class._meta.db_table
	model_list = list(model_class.objects.all()) 
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()
	form = selectForm2()
	if not field_list:
		create_field_list(model_class)
	model_id = field_list[0]
	print "field: ", model_id
	#form_class = get_fields_dynamic(m_tb_name)
	#form = form_class(request.POST)
	#z = remove_field_list(model_class) ###################################!!NOTE: removes field_list. you may need 
	if request.method == 'POST':
		if "_delete" in request.POST: 
			print "SLECTEDDDDDDDDDDDD SAYIN!"
			form = selectForm2(request.POST)
			if form.is_valid(): # All validation rules pass
				print "FORM VALID!"
		#### Below i have a possible approach to my problem on how to get a specific Attributes row using user submitted form data
		#### Attributes.objects.get(name=product_form.cleaned_data['select_fields']) 
				delete_items = form.cleaned_data['select_fields']
				for item in delete_items:
					print "items: ", item
####### mipws na ta vazeis ta items gia delete se mia lista  kai meta na ta svinei? opws ginetai sto katw comment...
#######	MyModel.objects.filter(id__in=request.POST.getlist('delete_list')).delete()
					instance = model_class.objects.get(**{field_list[2]:item}) # default returns the model's id if called i.e. "print instance"
					print "instance", instance 
###### gia na kaneis delete polla antikeimena mazi des kai to https://github.com/alex/django-filter app
					#model_class.objects.filter(id__in=request.POST.getlist('delete_list')).delete()
					instance.delete() #comment to stop delete
				messages.success(request, 'Selected fields deleted')
				#return HttpResponseRedirect('/Directories/') 
				return HttpResponseRedirect(reverse('Directories:index'))
			else:
				return HttpResponse('ERROR in POST -- Return to form submission')
		elif "_edit" in request.POST:
			print "You pressed update fields button in list template"
			form = selectForm2(request.POST)
			if form.is_valid(): # All validation rules pass
				print "selectForm VALID!"
				delete_items = form.cleaned_data['select_fields']
				print "delete items", str(delete_items)
				for item in delete_items:
					print "item: ", item
					instance = model_class.objects.get(**{field_list[2]:item}) # default returns the model's id if called i.e. "print instance"
					update_list.append(item)
					print "instance", instance
				# insert fields and their values into a dictionary
				for count in reversed(range(1, len(field_list))):
					f_val = getattr(instance, field_list[count])
					field_values[field_list[count]] = f_val
					print "sooooo we have field_values: ", field_values
					print count
					print field_list[count], ":", f_val			
#### to m_table to afinw etsi gia tin wra alla meta 8a to apo8ikeuw se session gia n diatireite metaksi selidwn. 
				url = "%s?m_table=attributes" % reverse('Directories:edit_models')
				return HttpResponseRedirect(url)
				#return render(request, 'Directories/edit.html', {"field_names": field_names, "update_list": update_list, "m_tb_name": m_tb_name})
			else:
				return HttpResponse('ERROR in POST -- Return to form submission')
	else:
		#form = form_class()
		form = selectForm2()
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/list.html', {'model_class':model_class, 'model_name': model_name, 
	'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 
	'model_name':model_name, 'form':form})
	
'''
	View that updates a selected field 
'''
#### ti prepei na kanw gia to update:
	### 1) ftiakse ena queryset pou 8a epistrefei to field row basi tou field pou dialeksame sto list template 
	### p.x. t = Attributes.objects.get(descr="chosen_field")
	### 2) xrisimopoise auto to queryset ('t') gia na allakseis tis times se ola ta fields... 
	### dld t.descr = 'your_value', t.notes = 'your_value' ktl
	### 3) kane t.save() gia na apo8ikeutoun oi allages!!! tooosssooooooooo APLA!
def modelEdit(request):
	print "list:", update_list
	#create a global list with the instances to be updated. This will be called in the modelEdit view
### gia to form 8elw apla na emfanisw ta fields kai dipla koutia pou 8a grafw ta names tous. Me to submit 8a stelnontai edw
### kai xrisimopoiwntas form.cleaned_data[] 8a ta epeksergazomai (me queryset??) kai meta save()
	mvar = request.GET.get('m_table')
	model_class = get_model('Directories', mvar)
	print "variable sent to edit is:", mvar
	for item in update_list:
		t = model_class.objects.get(**{field_list[2]:item})
	print "instance: ", t
	# Get the field values list from dlist as shown below and then show the values in the edit template, inside the textboxes
	f_val_list = sorted(field_values.items()) #sort puts them in alphabetical order but you may need to change this for other models
	print "field_values: ", f_val_list
	print "field_values: ", field_values
	form_class = get_dynamic_form(mvar)
	if "_alter" in request.POST:
		print "instance: ", t
		print "alter presseedddd!"
		#for item in update_list:
			#t = model_class.objects.get(**{field_list[2]:item})
		form = form_class(request.POST)#, instance=t)
		if form.is_valid(): # All validation rules pass
			print "instance: ", t
			print "form valid! now start updating fields!" 
			# use the values sent in the form to update the fields
			for count in range(1, len(field_list)):
				form_data = form.cleaned_data[field_list[count]]
				setattr(t, field_list[count], form_data)
				print "new field value is:", getattr(t, field_list[count])
			print "instance: ", t
			t.save()
			#send a message to inform users that form submission was a success
			messages.success(request, 'Selected fields updated')
			return HttpResponseRedirect(reverse('Directories:index'))
		else:
			print "form errors: ", form.errors
			return HttpResponse('ERROR -- Return to form submission')
	else:
		for item in update_list:
			t = model_class.objects.get(**{field_list[2]:item})
		form = form_class(instance=t)
		print "something not working or submit button not pressed"
	return render(request, 'Directories/edit.html', {'form':form, 'field_list':field_list, 'f_val_list':f_val_list})
	
'''
	View for adding a new row to a model dynamically.
'''
def modelUpdate(request):	
	print "Edit page"
	if 'model_classes_field' in request.GET:
		m_tb_name = request.GET['model_classes_field']
		print 'model_classes_field', m_tb_name
		model_class = get_model('Directories', m_tb_name)
		model_name = model_class.__name__
		field_names = model_class._meta.get_all_field_names()			
	if request.method == 'POST': 
		print "m_tb_name is: ", m_tb_name
		form_class = get_dynamic_form(m_tb_name)
		form = form_class(request.POST)	
		print "YEAHHHH!"			
		if form.is_valid(): # All validation rules pass
			print "WOOOHOOOO form is valid!" 
			# set commit=False to prevent saving into database"
			row = form.save() 
			form = dbForm()
			#send a message to inform users that form submission was a success
			messages.success(request, 'New model data created!')
			return HttpResponseRedirect(reverse('Directories:index'))
		else:
			print "form errors: ", form.errors
			return HttpResponse('ERROR -- Return to form submission')
		
	else:
		form_class = get_dynamic_form(m_tb_name)
		form = form_class() # An unbound form
		print "no form submission: ", form.errors
	return render(request, 'Directories/create.html', {'model_name':model_name, 'field_names':field_names})

#returns a list of field names
def create_field_list(model):
	print "list create "
	for f_name in model._meta.get_all_field_names():
		field_list.append(f_name)
	return field_list

def remove_field_list(model):
	print "list delete "	
	for f_name in model._meta.get_all_field_names():
		field_list.remove(f_name)
	return field_list
	
def get_model_fields(model):
	return model._meta.fields
  
def get_field_data(model, field):
	return model.objects.values_list(field, flat=True)
	
