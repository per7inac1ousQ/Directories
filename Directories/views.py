import datetime
from Directories.forms import dbForm, editForm, get_form
from Directories.models import Department, Attributes
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

def index(request): 
	form = dbForm()
	return render(request, 'Directories/index.html', {'form':form})

'''	if request.method == 'POST': # If the form has been submitted...
		#form = get_form()		
		form = dbForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			print "form valid -> now check submit button"
			if "_change" in request.POST:
				print "CHANGEEEEEEEEEEEEEEEEEEEEEEEEEEE"
			elif "_add" in request.POST:
				print "ADDDDDDDDDDDDDDDDDDDDDDDDD"
		else:
			print "form not validddd"
			print "form: ", form.errors
	else:
		form = dbForm()
		print "Post data were not sent"

	return render(request, 'Directories/index.html', {'form': form })
'''    

def dlist(request):
	if request.method == 'POST': # If the form has been submitted...
		print "post!!!"
		form = dbForm(request.POST) # A form bound to the POST data
		print "check data"
		if form.is_valid(): # All validation rules pass
			print "bound form, get data"
			model_classes_field = form.cleaned_data['model_classes_field']
			print "post data is: ", model_classes_field
			model_class = get_model('Directories', model_classes_field) 
			model_list = list(model_class.objects.all())
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
						c.append(f_name)			
						k.append(j)
					count += 1
			y = zip(c,k)
			asa = ''.join(column.rjust(10) for column in str(k))
			return render(request, 'Directories/list.html', {'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 'y':y, 'c':c, 'k':k, 'asa':asa, 'data_list':data_list})
		else:
			print "form errors: ", form.errors
	else:
		form = dbForm() # An unbound form
		print "no POST - form: ", form.errors
		print "unbound form"
	#get the model id selected in the POST form and convert it to an integer
	print "chooopp welc to list"
	m_tb_name= request.POST.get('model_classes_field')
	print 'You searched for: %r' % m_tb_name       
	model_class = get_model('Directories', m_tb_name) 
	model_list = list(model_class.objects.all())
	# find the column length or number of rows of a column for given query (model_list)
	#col_length = get_length(model_class, model_list)
 	#print "column length: ", col_length
	#for mod in model_list:
	#		model_list.append("Edit") ################### Kane uncomment autes tis duo grammes gia na deis ama ginetai append to "Edit" sta stoixeia tou pinaka... mipws na xrisimopoiiseis UNION operations '|' gia na enwseis ta duo QuerySet
	#initialise fields and their names
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()
	#for f_name in field_names:	
		#data_list = list(get_field_data(model_class, f_name))
	data_list = list(get_field_data(model_class, "attr_id"))
	#row = model_class.objects.get(attr_id='?').values()
	if not field_list:
		z = create_field_list(model_class)#[count]
		print "field_list: ", z
		count = 0
		for f_name in field_names:	
			for mod in model_list:
				j = getattr(mod, field_list[count])
				c.append(f_name)			
				k.append(j)
				#j = j.encode('ISO 8859-7')
				#j = j.encode('windows-1253').decode('utf-8')
			count += 1

	#z = remove_field_list(model_class) ###################################!!NOTE: removes field_list. you may need it
	y = zip(c,k)
	#pagination(model_list, 25) ##############################################??????
	asa = ''.join(column.rjust(10) for column in str(k))
	return render(request, 'Directories/list.html', {'m_tb_name':m_tb_name, 'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 'y':y, 'c':c, 'k':k, 'asa':asa, 'data_list':data_list})

def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def modelUpdate(request):
	data = {
     'form-TOTAL_FORMS': u'2',
     'form-INITIAL_FORMS': u'0',
     'form-MAX_NUM_FORMS': u'',
     'form-0-title': u'Test',
     'form-0-pub_date': u'1904-06-16',

     'form-1-title': u'Test',
	}
	editFormSet = formset_factory(editForm)#, extra=len(field_names))
	formset = editFormSet(data)
	for form in formset:
		print(form.as_table())
	return render(request, 'Directories/create.html', {'formset':formset})


def modelUpdate2(request, model_id):
	#test model formset ##############################################
	AttrFormSet = modelformset_factory(Attributes, extra=1)#, widgets={"descr": Textarea(), "attr_id":Textarea()})
	formset = AttrFormSet()
	print(formset)
	### end test ##############################################
	try:	
		req_data = Attributes.objects.get(pk=model_id)
		#fields_len = len(req_data) #??????????????????????
        #req_data = Attributes.objects.values_list(flat=True).get(pk=id)
	except Attributes.DoesNotExist:
		raise Http404    
	field_names = Attributes._meta.get_all_field_names()
	print req_data
	data = {
     'form-TOTAL_FORMS': u'2',
     'form-INITIAL_FORMS': u'0',
     'form-MAX_NUM_FORMS': u'',
     'form-0-title': u'Test',
     'form-0-pub_date': u'1904-06-16',

     'form-1-title': u'Test',
	}
	#initialised a formset for handling dynamic field input	
	editFormSet = formset_factory(editForm)#, extra=len(field_names))
	formset = editFormSet(data)
	for form in formset:
		print(form.as_table())

	return render(request, 'Directories/create.html', {'req_data':req_data, 'field_names':field_names, 'formset':formset})
    #return HttpResponse("You are looking at item with id = %s." % pk)	


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

def get_model_fields(model):
	return model._meta.fields

def get_field_data(model, field):
	return model.objects.values_list(field, flat=True)

def attrUpdate(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

