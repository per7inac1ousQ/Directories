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
	return field_classes

class loginForm(forms.Form):
	user = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models())#, required=True,) # maybe not include required=True"
	
#class listForm(forms.Form):
#	mod_classes = forms.ChoiceField(choices=models())
	
class editForm(forms.Form):
	field = forms.CharField()

#class searchForm(forms.Form):
#	field = forms.TextField()
	
#create a ModelForm using a dynamic model
def get_dynamic_form(c_model):
	model_class = get_model('Directories', c_model)	
	class ObjForm(forms.ModelForm):
	    class Meta:
	        model = model_class
	return ObjForm

class selectForm(forms.Form):
	select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
	
class selectForm2(forms.Form):
	def __init__(self, *args, **kwargs):
		choices = kwargs.pop('my_choices')
		super(selectForm2, self).__init__(*args, **kwargs)
		#initialise multiple select checkboxes with id = checkFields.
		self.fields["select_fields"] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'id': 'checkFields'}), choices=choices)
	
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
