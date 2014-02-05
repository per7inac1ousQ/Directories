#!/usr/bin/python
# -*- coding: iso-8859-7 -*-
import datetime
import itertools
from Directories.forms import dbForm, editForm, get_dynamic_form, selectForm, get_fields_dynamic
from Directories.models import Department, Attributes, Employees, Instructors, Katefth, KatefthKykloi, Kykloi, KykloiExamina, ModuleKykloi, Modules, ModulesTutors, PubInstr, PubTypes, Publications, Ranks, Service, Users, Works
from django import forms
from django.core import serializers
from django.db.models import get_models, get_app, get_model
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import loader, RequestContext
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.template import Template
from django.core.paginator import Paginator
from django.http import Http404
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms import Textarea
from django.contrib import messages
#import django_tables as tables 

model_classes = []
field_classes = []
fields_dict = []
field_list = []
field_models = []
k = []
c = []
instance_list = []

def index(request): #for two submit buttons:
	print "start"
	form = dbForm()
	if request.method == 'GET':	
		print "get!!!"
		if '_change' in request.GET:
			cform = dbForm(request.GET, prefix="change") 
			print "i am in _change submit button"
			if cform.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = cform.cleaned_data['model_classes_field']		
				return render(request, 'Directories/list.html', {'model_classes_field':model_classes_field})
			else:
				return HttpResponse('ERROR in GET -- Return to form submission')
		elif '_add' in request.GET:
			aform = dbForm(request.GET, prefix="add")
			print "i am in _add submit button"
			if aform.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = aform.cleaned_data['model_classes_field']		
				return render(request, 'Directories/create.html', {'model_classes_field':model_classes_field})
			else:
				return HttpResponse('ERROR in GET -- Return to form submission')
	else:
		cform = dbForm(prefix="change")
		aform = dbForm(prefix="add")
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
	if not field_list:
		z = create_field_list(model_class)
	#form_class = get_fields_dynamic(m_tb_name)
	#form = form_class(request.POST)
	#z = remove_field_list(model_class) ###################################!!NOTE: removes field_list. you may need 
	if request.method == 'POST':
		if "_selected" in request.POST:
			print "SLECTEDDDDDDDDDDDD SAYIN!"
			form = selectForm(request.POST)
			#form.fields[field_list[1]].queryset = model_class.objects.filter(user=request.user)
			if form.is_valid(): # All validation rules pass
				print "FORM VALID!"
		#### Below i have a possible approach to my problem on how to get a specific Attributes row using user submitted form data
		#### Attributes.objects.get(name=product_form.cleaned_data['select_fields']) 
				delete_items = form.cleaned_data['select_fields']
				for item in delete_items:
					print "items: ", item
					instance = model_class.objects.get(**{field_list[2]:item}) # default returns the model's id if called i.e. "print instance"
		# to display all attributes u can use instance.attrs.all() found in eav-django app
					print "instance", instance 
					instance.delete() #comment to stop delete
				messages.success(request, 'Selected fields deleted')
				#prepei na kanei allou redirect oxi sto index gt ginetai axtarmas afou kanei xrisi tou selectForm oxi tou dbForms
				return render(request, 'Directories/index.html')
			else:
				return HttpResponse('ERROR in POST -- Return to form submission')
		elif "_edit" in request.POST:
			print "You pressed update fields button in list template"
			form = selectForm(request.POST)
			if form.is_valid(): # All validation rules pass
				print "selectForm VALID!"
				delete_items = form.cleaned_data['select_fields']
				for item in delete_items:
					print "item: ", item
					instance = model_class.objects.get(**{field_list[2]:item}) # default returns the model's id if called i.e. "print instance"
		# to display all attributes u can use instance.attrs.all() found in eav-django app
					print "instance", instance 		
					instance_list.append(instance)
				messages.success(request, 'Selected fields updated')
				#prepei na kanei allou redirect oxi sto index gt ginetai axtarmas afou kanei xrisi tou selectForm oxi tou dbForms
				return render(request, 'Directories/create.html', {"instance_list": instance_list, "m_tb_name": m_tb_name})
			else:
				return HttpResponse('ERROR in POST -- Return to form submission')
	else:
		#form = form_class()
		form = selectForm()
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/list.html', {'model_class':model_class, 'model_name': model_name, 
	'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 
	'model_name':model_name, 'form':form})
	
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
		#if '_update' in request.POST: # If the form has been submitted...
		print "m_tb_name is: ", m_tb_name
		form_class = get_dynamic_form(m_tb_name)
		form = form_class(request.POST)	
		if 'select_fields' in request.POST:
			print "One step closer to delete", m_tb_name
			updated_item = request.POST.get('select_fields')
			print "item: ", updated_item
			print "instance list: ", form.instance
			if form.is_valid(): # All validation rules pass
				print "form valid! now start updating fields!" 
				return HttpResponse('One step closer to updating your fields')
			else:
				print "form errors: ", form.errors
				return HttpResponse('ERROR -- Return to form submission')
		else:
			print "YEAHHHH!"			
			if form.is_valid(): # All validation rules pass
				print "WOOOHOOOO form is valid!" 
				# set commit=False to prevent saving into database"
				row = form.save() 
				form = dbForm()
				#send a message to inform users that form submission was a success
				messages.success(request, 'Model details updated.')
				return render(request, 'Directories/index.html', {'form': form}) 
			else:
				print "form errors: ", form.errors
				return HttpResponse('ERROR -- Return to form submission')
			
	else:
		form = dbForm() # An unbound form
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
	print "POST request received: "	
	print request.POST['model_classes_field']
	m_tb_name= request.POST['model_classes_field']
	model_class = get_model('Directories', m_tb_name)
	mod = get_model('Directories', 'katefth_kykloi')
	print "problematic table:"
	print model_class	
	print "new mod object: "
	print mod
#	model_list = model_class.objects.all()
	print 'You searched for: %r' % m_tb_name
# take the model_name through POST and populate the tables....
	return render(request, 'Directories/list.html', {'m_tb_name':m_tb_name, 'model_class':model_class})

#Method to get element rows found in dlist view
'''
def get_rows(model):
	f_count = 0
	rows = []
	for mod in model_list:
		for field in field_list:
			fields_lst= list(model_class.objects.values_list(field, flat=True))
			rows.append(fields_lst[f_count])
			f_count += 1
	return rows
'''
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

'''
def index2(request): #for two submit buttons:
	print "start"
	form = dbForm()
	print "form is: ", form
 	return render(request, 'Directories/index.html', {'form':form})
'''	
		
'''
def dlist2(request):
	print "list page"
	#Here I handle the form data from the index view and create the list template that displays the model objects
	if request.method == 'GET':	
		form = dbForm(request.GET) # A form bound to the GET data
		print "get!!!"
		if form.is_valid(): # All validation rules pass
			print "bound form, get data"
			model_classes_field = form.cleaned_data['model_classes_field']
			model_class = get_model('Directories', model_classes_field)
			model_name = model_class._meta.db_table
			model_list = list(model_class.objects.all()) 
			fields = get_model_fields(model_class)
			field_names = model_class._meta.get_all_field_names()
			if not field_list:
				z = create_field_list(model_class)
				count = 0
				for f_name in field_names:	
					for mod in model_list:
						j = getattr(mod, field_list[count])
						#j = j.encode('ISO 8859-7')
						#j = j.encode('windows-1253').decode('utf-8')
						c.append(f_name)			
						k.append(j)
					count += 1
			y = zip(c,k)
			
	# other try ###################################################
			f_count = 0
			result_list = []
			for field in field_list:
				fields_lst= list(model_class.objects.values_list(field, flat=True))
				#for value in fields_lst:
				result_list.append(fields_lst)
			f_count += 1
	# to list rows kanei miksi ta lists wste na vgainoun se morfi rows####################################
			f_count = 0
			rows = []
			chk_ls = []
			for mod in model_list:
				chk_ls.append("<input type='checkbox' />")
				for field in field_list:
					fields_lst= list(model_class.objects.values_list(field, flat=True))
					#for value in fields_lst:
					rows.append(fields_lst[f_count])
				f_count += 1
			#z = remove_field_list(model_class) ###################################!!NOTE: removes field_list. you may need it
			return render(request, 'Directories/list.html', {'model_class':model_class, 'model_name': model_name, 
			'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 'y':y, 'c':c, 
			'k':k, 'model_name':model_name, 'rows': rows, 'result_list':result_list, 'f_count':f_count, 'chk_ls':chk_ls,
			'sForm':sForm})
		else:
			return HttpResponse('ERROR in GET -- Return to form submission')
	# since i created my list template now I check the form 
	elif request.method == 'POST':
		print "SLECTEDDDDDDDDDDDD SAYIN!"
		print "YEAHHHH!"
		#form_class = get_fields_dynamic (request.GET['model_classes_field'])
		#form = form_class(request.POST)
		#sForm = selectForm(request.POST)
		sForm = selectForm(request.POST)
		if sForm.is_valid(): # All validation rules pass
			print "FORM VALID!"
			#form = dbForm() # form or sForm??
			messages.success(request, 'Selected fields deleted')
			return render(request, 'Directories/index.html', {'sForm':sForm}) # form or sForm??
		else:
			return HttpResponse('ERROR in POST -- Return to form submission')
	else:
		#sForm = selectForm()
		form = dbForm()
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/list.html', {'form':form})
'''

'''
def modelUpdate2(request):	
	print "Edit page"
	if request.method == 'GET': 
		if 'model_classes_field' in request.GET: # If the form has been submitted...
			print "get!!!", request.GET['model_classes_field']
			#model_classes_field = request.POST['model_classes_field']
			#model_class = get_model('Directories', model_classes_field)
			form = dbForm(request.GET) # A form bound to the GET data
			#form = get_dynamic_form(request.GET['model_classes_field'])
			print "check data"
			if form.is_valid(): # All validation rules pass
				model_classes_field = form.cleaned_data['model_classes_field']
				print "get data is: ", model_classes_field
				model_class = get_model('Directories', model_classes_field)
				#form = get_dynamic_form(model_classes_field)
				#get model's name
				model_name = model_class.__name__
				field_names = model_class._meta.get_all_field_names()			
				return render(request, 'Directories/create.html', {'model_name':model_name, 'field_names':field_names})
			else:
				print "form errors: ", form.errors
				return render(request, 'Directories/index.html')
	elif request.method == 'POST': 
		if 'update' in request.POST: # If the form has been submitted...
			print "YEAHHHH!"
			form_class = get_dynamic_form(request.GET['model_classes_field'])
			form = form_class(request.POST)			
			if form.is_valid(): # All validation rules pass
				print "WOOOHOOOO form is valid!" 
				print "Uncomment line below to save to database"
				row = form.save(commit=False) 
				form = dbForm()
				#send a message to inform users that form submission was a success
				messages.success(request, 'Model details updated.')
				return render(request, 'Directories/index.html', {'form': form}) 
			else:
				print "form errors: ", form.errors
				return HttpResponse('ERROR -- Return to form submission')
	else:
		form = dbForm() # An unbound form
		print "no form submission: ", form.errors
'''
