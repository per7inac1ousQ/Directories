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
from django.template import Template
from django.core.paginator import Paginator
from django.http import Http404


model_classes = []
field_list = []
field_models = []
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
	return model_classes

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

def get_field_data(model, field):
	return model.objects.values_list(field, flat=True)

def create(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def attrUpdate(request):
	dir_list = Department.objects.all()
	return render(request, 'Directories/create.html', {'dir_list': dir_list})

def dlist(request):
	#get the model id selected in the POST form and convert it to an integer
	m_tb_name= request.POST.get('model_classes_field')
	print 'You searched for: %r' % m_tb_name
	model_class = get_model('Directories', m_tb_name)
	model_list = model_class.objects.all() 
	#initialise fields and their names
	fields = get_model_fields(model_class)
	field_names = model_class._meta.get_all_field_names()
################ edw exei ena 8ema checkare to!! #######	
	#for f_name in field_names:	
		#get_field_d = model_class.objects.filter('%s', [f_name])
###################################################
	for f_name in field_names:	
		data_list = list(get_field_data(model_class, f_name))
	#row = model_class.objects.get(attr_id='?').values()

	if not field_list:
		z = create_field_list(model_class)#[count]
		print "field_list: ", z
		count = 0
		field_counter = 0
		for f_name in field_names:	
			
			for mod in model_list:
				j = getattr(mod, field_list[count])
				print j	
				#strj = '''<td> %s </td>''' %j		
				c.append(f_name)	
				#k.append(strj)				
				k.append(j)
				
				#j = j.encode('ISO 8859-7')
				#j = j.encode('windows-1253').decode('utf-8')
			count += 1
	#z = remove_field_list(model_class) ##!!NOTE: removes field_list. you may need it
	y = zip(c,k)
	#first_elem = [i[0] for i in y]
	#if request.GET.get('model_fields'):
		#fields = request.GET.get('model_fields')
		#questions = model_class.objects.filter(query__icontains=model_fields)
	#pagination(model_list, 25) #######################??????
	#strj = '\n'.join(str(p) for p in k) 
	asa = ''.join(column.rjust(10) for column in str(k))
	#for row in k:
		#for column in str(row):
			#print ''.join(str(column).rjust(10))	
#	if request.method == 'GET':
		#form = editForm(request.GET)
		#if form.is_valid():

		#	return HtpResponseRedirect('/thanks')
		#else:
			#form = ContactForm() # An unbound form

   		 #return render(request, 'create.html', {
        #'form': form,
   		#})
	return render(request, 'Directories/list.html', {'m_tb_name':m_tb_name, 'model_class':model_class, 'model_list':model_list, 'fields':fields, 'field_names':field_names, 'field_list':field_list, 'y':y, 'c':c, 'k':k, 'asa':asa, 'data_list':data_list})

def modelUpdate(request, model_id):
    #pk=4
    try:	
		req_data = Attributes.objects.get(pk=model_id)
		#fields_len = len(req_data) #??????????????????????
        #req_data = Attributes.objects.values_list(flat=True).get(pk=id)
    except Attributes.DoesNotExist:
        raise Http404    
    field_names = Attributes._meta.get_all_field_names()
    print req_data
    return render(request, 'Directories/create.html', {'req_data':req_data, 'field_names':field_names})
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

class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models(), required=True,)


#class editForm(forms.Form):
#	id_field = forms.CharField(id)
	

#class listForm(forms.Form):
	#model_fields = forms.ChoiceField()



