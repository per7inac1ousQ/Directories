#!/usr/bin/python
# -*- coding: iso-8859-7 -*-
from django import forms
from django.db.models import get_models, get_app, get_model
from Directories.models import Attributes
from django.contrib.contenttypes.models import ContentType

model_classes = []
field_classes = []

def models():
	apps = get_app('Directories')
	for model in get_models(apps):
		model_classes.append( (model._meta.verbose_name, model._meta.db_table), )
	return model_classes

def fields():
	m_values = Attributes.objects.values_list('descr', flat=True)
	for val in m_values:
		field_classes.append((val, val))
	print "list: ", field_classes
	return field_classes

class loginForm(forms.Form):
	user = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models())#, required=True,) # maybe not include required=True"
	
class editForm(forms.Form):
	field = forms.CharField()

#create a ModelForm using a dynamic model
def get_dynamic_form(c_model):
	model_class = get_model('Directories', c_model)	
	class ObjForm(forms.ModelForm):
	    class Meta:
	        model = model_class
	return ObjForm

class selectForm2(forms.Form):
	select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
	
class selectForm(forms.Form):
	#select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
	def __init__(self, *args, **kwargs):
		choices = kwargs.pop('field_choices')
		super(selectForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields["select_fields"] = forms.ChoiceField(choices=choices)
		#select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
		#self.fields["select_fields"].widget = forms.CheckboxSelectMultiple()
		#self.fields["my_field"] = forms.ChoiceField(choices=choices)   exampleeeee
	
def get_fields_dynamic(c_model):
	model_class = get_model('Directories', c_model)	
	class selectForm(forms.ModelForm):
	    class Meta:
	        model = model_class
		def __init__(self, *args, **kwargs):
			super(selectForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
			#select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
			self.fields["descr_en"].widget = forms.CheckboxSelectMultiple()
			self.fields["descr_en"].choices = fields()
	return selectForm  


'''
# old models() method that iterates through all of the models in the database and 
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

'''
