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
	m_values = Attributes.objects.values_list('descr_en', flat=True)
	for val in m_values:
		field_classes.append((val, val))
	return field_classes
	
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

class selectForm(forms.Form):
	select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=fields())
	
##################################### dynamic try
class selectForm2(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super(selectForm, self).__init__(*args, **kwargs)
        self.fields["select_fields"] = forms.ChoiceField(choices=choices)
##################################        

def get_fields_dynamic(c_model):
	model_class = get_model('Directories', c_model)	
	class selectForm(forms.ModelForm):
	    class Meta:
	        model = model_class
	        fields = ['descr']
		def __init__(self, *args, **kwargs):
			super(selectForm, self).__init__(*args, **kwargs)
			self.fields["descr"].widget = forms.CheckboxSelectMultiple()
			form.fields["descr"].queryset = model_class.objects.all()
	return selectForm  

############ dokimase na kaneis render tin form sto template opws ekanes me to create.html kai oxi apla {{form.as_p}}
##### ara 8a valeis p.x. "for val in attributes.objects.value_list('descr'): {{val}}" i kati tetoio tespa
'''
# CHECK THESE EXAMPLES
class NewForm(forms.Form):
    super(NewForm, self).__init__(*args, **kwargs)
    def __init__(self, choices, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        self.fields["choices"] = forms.ChoiceField(choices=choices)
        

class MyForm(BaseForm):
    afield = forms.ChoiceField(choices=INITIAL_CHOICES)
	def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['afield'].choices = my_computed_choices
'''

#works with checkboxes but models NOT fields
class selectForm2(forms.Form): #widget=forms.CheckboxSelectMultiple, valto stin paren8esi molis sou doulepsi me dropdown list box
	select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=models())

'''	
class selectForm(forms.Form):
	select_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=models())
	def __init__ (self, *args, **kwargs):
        brand = kwargs.pop("brand")
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields["diets"].widget = forms.widgets.CheckboxSelectMultiple()

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
