#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import ldap
import datetime
import itertools
import collections
import logging
from django_auth_ldap.backend import LDAPBackend
from Directories.forms import dbForm, editForm, get_dynamic_form, selectForm, selectForm2, get_fields_dynamic, loginForm
from Directories.models import Department, Attributes, Employees, Instructors, Katefth, KatefthKykloi, Kykloi, KykloiExamina, ModuleKykloi, Modules, ModulesTutors, PubInstr, PubTypes, Publications, Ranks, Service, Users, Works
from django import forms
from django.core import serializers
from django.db.models import get_models, get_app, get_model
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import loader, RequestContext
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import Template
from django.core.paginator import Paginator
from django.http import Http404
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms import Textarea
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.utils import simplejson
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView


model_classes = []
field_choices = []
fields_dict = []
field_list = []
field_models = []
field_values = {}
k = []
c = []
update_list = []
	
def user_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('Directories:index'))
	form = loginForm()
	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['user']
			password = form.cleaned_data['password']
			print "user is:", username, "with password", password
			# authenticate user
			user = authenticate(username=username, password=password)
			if user is not None:
				# the password verified for the user
				if user.is_active:
					login(request, user)
					print("User is valid, active and authenticated")
					return HttpResponseRedirect(reverse('Directories:index'))
					#return HttpResponse('Successful Authentication!')
				else:
					print("The password is valid, but the account has been disabled!")
					return HttpResponse('Account disabled.')
			else:
				# the authentication system was unable to verify the username and password
				messages.error(request, 'username and/or password were incorrect.')
				return HttpResponseRedirect(reverse('Directories:login'))
				#return HttpResponse('The username and password were incorrect.')
			print "user is:", user, "with password", password
		else:
			return HttpResponse('ERROR in GET -- Return to form submission')
	else:
		form = loginForm()
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/login.html', {'form':form})
	
@login_required(login_url='Directories:login')
def index(request): #for two submit buttons:
	print "start"
	#check that model table name is not stored in the session before initiating it
	if 'model_table' in request.session:
		###print fields(request, 'descr') damn fields() runs here
		print "session model_table is:", request.session['model_table']
		del request.session['model_table']	
	else:
		print "session model_table became null"
	form = dbForm()
	if request.method == 'GET':	
		print "get!!!"
		# ifs not working for some reason.... they are useless as they are
		if "_change" in request.GET:
			form = dbForm(request.GET) 
			print "i am in _change submit button"
			if form.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = form.cleaned_data['model_classes_field']
				request.session['model_table'] = model_classes_field	
				return HttpResponseRedirect(reverse('Directories:list_models'))		
			else:
				print "no POST - form: ", form.errors
				return HttpResponse('ERROR in GET -- Return to form submission', form.errors)
		elif '_add' in request.GET:
			form = dbForm(request.GET)
			print "i am in _add submit button"
			if form.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = form.cleaned_data['model_classes_field']
				request.session['model_table'] = model_classes_field	
				return HttpResponseRedirect(reverse('Directories:update_directories'))	
			else:
				print "no POST - form: ", form.errors
				return HttpResponse('ERROR in GET -- Return to form submission', form.errors)
		else:
			print "WTF??"
	else:
		form = dbForm()
		print "no POST - form: ", form.errors
		print "unbound form"
 	return render(request, 'Directories/index.html', {'form':form})

'''
	View that displays a list of all model objects
'''
@login_required(login_url='Directories:login')
def dlist(request):
	print "list page"
	#request.session['model_table'] = 'Department' #### auto to dialegei apo to index
#print "request.session = ", request.session['model_table']
#fields(request, 'descr')
#print "fields ", get
	#or you can model_class = request.session['model_table'] but need to serialize with JSON first so as to convert from unicode to class object or sth like that
	m_tb_name = request.GET['model_classes_field'] # get the model table name
	model_class = get_model('Directories', m_tb_name) #request.session['model_table']) #################################
	print "name ", m_tb_name
	print "class ", model_class
	model_name = model_class._meta.db_table
	model_list = list(model_class.objects.all()) 
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()
##################### check form here
	form = selectForm2(my_choices = field_choices)
	if not field_list:
		create_field_list(model_class)
#the fields() function start
	#if 'model_table' in request.session:	
		#m_name = request.session['model_table']
		#model_class = get_model('Directories', m_name)
		model_class = get_model('Directories', m_tb_name)
		m_values = model_class.objects.values_list(field_list[1], flat=True) 
		for val in m_values:
			field_choices.append( (val, val), )
		#the fields() function end
		print 'field_choices', field_choices
	else:
		print "session variable model_table became null"
	#form_class = get_fields_dynamic(m_tb_name)
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
				items = [value.encode("utf8") for value in delete_items]
				for item in items:
					print "items: ", item
#######	MyModel.objects.filter(id__in=request.POST.getlist('delete_list')).delete()
					instance = model_class.objects.get(**{field_list[1]:item}) # default returns the model's id if called i.e. "print instance"
					print "instance", instance 
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
				edit_items = form.cleaned_data['select_fields']
				items = [value.encode("utf8") for value in edit_items]
				for item in items:
					print "item: ", item
					instance = model_class.objects.get(**{field_list[1]:item}) # default returns the model's id if called i.e. "print instance"
					update_list.append(item)
				# insert fields and their values into a dictionary
				for count in reversed(range(1, len(field_list))):
					f_val = getattr(instance, field_list[count])
					field_values[field_list[count]] = f_val
					print "sooooo we have field_values: ", field_values
					print count
					#print field_list[count], ":", f_val			
#### to m_table to afinw etsi gia tin wra alla meta 8a to apo8ikeuw se session gia n diatireite metaksi selidwn. 
				#url = "%s?m_table=attributes" % reverse('Directories:edit_models')
				return HttpResponseRedirect(reverse('Directories:edit_models'))
# prepei kapws na steilw to update_list ------> return render_to_response('Directories/edit.html', {'update_list':update_list, 'field_list':field_list}, context_instance=RequestContext(request))
			else:
				return HttpResponse('ERROR in POST -- Return to form submission')
	else:
######## check form to have checkboxes
		form = selectForm2(my_choices = field_choices)
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/list.html', {'model_class':model_class, 'model_name': model_name, 
	'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 
	'model_name':model_name, 'form':form})
	
'''
	View that updates a selected field. The idea is to create a queryset that will as an argument the field value that was
	posted in the list template. Then use a form to gather user input for the new values and after the form is valid assign 
	these to the corresponding queryset fields. In the end, the newly queryset has been made and you can save it in the DB.
'''
@login_required(login_url='Directories:login')
def modelEdit(request):
	print "Edit page"
	#create a global list with the instances to be updated. This will be called in the modelEdit view
	#mvar = request.GET.get('m_table')
	mvar = request.session['model_table']
	model_class = get_model('Directories', mvar)
	print "variable sent to edit is:", mvar
	#print "id", field_list[0]
	#import pdb; pdb.set_trace()  for debugging but do not know how it works....
	# create querysets using the field chosen in the list template
	print 'update_list length:', len(update_list)
	for item in update_list:
		# i vale get_or_create() -->> p.x. rate, created = VideoRate.objects.get_or_create()
		t = model_class.objects.get(**{field_list[1]:item})
	#print "instance: ", t
	# Get the field values list from dlist as shown below and then show the values in the edit template, inside the textboxes
	f_val_list = sorted(field_values.items()) #sort puts them in alphabetical order but you may need to change this for other models
	# maybe use model FORMSET instead ??
	form_class = get_dynamic_form(mvar)
	if "_alter" in request.POST:
		#print "instance: ", t
		print "alter presseedddd!"
		form = form_class(request.POST)#, instance=t)
		if form.is_valid(): # All validation rules pass
			#print "instance: ", t
			print "form valid! now start updating fields!" 
			# use the form data to change the queryset 't' field values
			print 'start forloop', len(field_list)
			for count in range(1, len(field_list)):
				form_data = form.cleaned_data[field_list[count]]
				print "FORM DATA:", form_data.encode("utf8")
				setattr(t, field_list[count], form_data)
				print "data", getattr(t, field_list[count]).encode("utf8")
			print 'end forloop'
			#print "FORM DATA2:", form_data
			##### alles epiloges gia to t:
			##### Foo.objects.get(pk=????).update(**data) opou data = {'field1': 'value1', 'field5': 'value5', 'field7': 'value7'}
			##### i kanw Foo.objects.get(pk=????).update(**{field_list[2]:item})
			# after changing the queryset data you can now save to database
			t.save()
			#send a message to inform users that form submission was a success
			messages.success(request, 'Selected fields updated') # kalw ama kanei duplicate la8os na epistrefei validate_unique()
			return HttpResponseRedirect(reverse('Directories:index')) 
		else:
			print "form errors: ", form.errors
			return HttpResponse('ERROR -- Return to form submission')
	else:
		for item in update_list:
			t = model_class.objects.get(**{field_list[1]:item})
		form = form_class(instance=t)
		print "something not working or submit button not pressed"
	return render(request, 'Directories/edit.html', {'form':form, 'field_list':field_list, 'f_val_list':f_val_list})
	
'''
	View for adding a new row to a model dynamically.
'''
@login_required(login_url='Directories:login')
def modelUpdate(request):	
	print "Creation page"
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

'''
	Logs out a user
'''
def user_logout(request):
	logout(request)
	messages.success(request, 'Succesfully logged out') 
	return HttpResponseRedirect(reverse('Directories:login'))
	
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
	
def fields(request, field):
	m_name = request.session['model_table']   # or you can model_class = request.session['model_table'] but need to serialize with JSON first
	model_class = get_model('Directories', m_name)
	m_values = model_class.objects.values_list(field, flat=True) # field = field_list[2]
	for val in m_values:
		field_choices.append( (val, val), )
	return field_choices
	
def models():
	apps = get_app('Directories')
	for model in get_models(apps):
		model_classes.append( (model._meta.verbose_name, model._meta.db_table), )
	return model_classes
