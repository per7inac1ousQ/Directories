import datetime
from Directories.forms import dbForm, editForm, get_dynamic_form
from Directories.models import Department, Attributes
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
#import django_tables as tables 


model_classes = []
field_list = []
field_models = []
k = []
c = []

def index(request): #for two submit buttons:
	form = dbForm()
 	return render(request, 'Directories/index.html', {'form':form})
# 1) check if POST data is sent and create two forms (maybe assign the same name)
# 2) check if valid
# 3) if valid check which submit button was pressed and render to the appropriate template (change -> list.html OR add -> create.html)
'''	if request.method == 'POST': # If the form has been submitted...
		print "post!!!"
		form = dbForm(request.POST) # A form bound to the POST data
		print "check data"
		if form.is_valid(): # All validation rules pass
			print "bound form, get data"
			model_classes_field = form.cleaned_data['model_classes_field']
			print "post data is: ", model_classes_field
		else:
			print "form errors: ", form.errors
	else:
		form = dbForm() # An unbound form
		print "no POST - form: ", form.errors
		print "unbound form"
	return render(request, 'Directories/index.html', {'url': url})'''
# WORKSSSSS! with the two lines	
	#form = dbForm()
 	#return render(request, 'Directories/index.html', {'form':form})
 
'''  if request.method == 'POST': # If the form has been submitted...
 +    #form = get_form()    
      form = dbForm(request.POST) # A form bound to the POST data
      if form.is_valid(): # All validation rules pass
 -      model_classes_field = form.cleaned_data['model_classes_field']
 -      return HttpResponseRedirect('/list/') # Redirect after POST
 +      print "form valid -> now check submit button"
 +      if "_change" in request.POST:
 +        print "CHANGEEEEEEEEEEEEEEEEEEEEEEEEEEE"
 +      elif "_add" in request.POST:
 +        print "ADDDDDDDDDDDDDDDDDDDDDDDDD"
      else:
 +      print "form not validddd"
        print "form: ", form.errors
    else:
 -    form = dbForm() # An unbound form
 -    print "form: ", form.errors
 -    print "not valiiiid form"
 -
 -  return render(request, 'Directories/index.html', {
 -    'form': form,
 -  })
 +'''

def dlist(request):
	print "list page"
	if request.method == 'GET':
		if 'model_classes_field' in request.GET: # If the form has been submitted...
			print "get!!!"
			form = dbForm(request.GET) # A form bound to the GET data
			#print "check data", request.post.get("model_classes_field")
			if form.is_valid(): # All validation rules pass
				print "bound form, get data"
				model_classes_field = form.cleaned_data['model_classes_field']
				print "post data is: ", model_classes_field
				model_class = get_model('Directories', model_classes_field) 
				model_list = list(model_class.objects.all())
				#		model_list.append("Edit") ################### Kane uncomment autes tis duo grammes gia na deis ama ginetai append to "Edit" sta stoixeia tou pinaka... mipws na xrisimopoiiseis UNION operations '|' gia na enwseis ta duo QuerySet
				fields = get_model_fields(model_class)
				field_names = model_class._meta.get_all_field_names()
				data_list = list(get_field_data(model_class, "attr_id"))
				if not field_list:
					z = create_field_list(model_class)#[count]
					print "field_list: ", z
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
				#z = remove_field_list(model_class) ###################################!!NOTE: removes field_list. you may need it
				asa = ''.join(column.rjust(10) for column in str(k))
				return render(request, 'Directories/list.html', {'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 'y':y, 'c':c, 'k':k, 'asa':asa, 'data_list':data_list})		
			else:
				print "form errors: ", form.errors
				return HttpResponse("-- ERROR: Please return to form submission --")
		elif request.method == 'POST': 
			if 'update' in request.POST: # If the form has been submitted...
				print "POST form from edit view sent!"
	#elif request.method == 'POST' and {{f_name}} in request.POST:
		#print "YEAH"
	else:
		form = dbForm() # An unbound form
		print "no POST - form: ", form.errors
		print "unbound form"
		return render(request, 'Directories/index.html')

def modelUpdate(request):	
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
				#row = form.save() #saves to database!!
				return render(request, 'Directories/list.html')
			else:
				print "form errors: ", form.errors
				return render(request, 'Directories/create.html')
	else:
		form = dbForm() # An unbound form
		print "no form submission: ", form.errors
	

#Xreiazzeeetaaaiiiiiiiiii??????????????????????????
def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

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
  
def attrUpdate(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

