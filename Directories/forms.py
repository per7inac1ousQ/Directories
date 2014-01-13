from django import forms
from django.db.models import get_models, get_app, get_model
from Directories.models import Attributes
from django.contrib.contenttypes.models import ContentType

model_classes = []

def models():
	apps = get_app('Directories')
	for model in get_models(apps):
		model_classes.append( (model._meta.verbose_name, model._meta.db_table), )
	return model_classes

#class dbForm(forms.Form):
#	model_classes_field = forms.ChoiceField(choices=models(), required=True,)

class dbForm(forms.Form):
	model_classes_field = forms.ChoiceField(choices=models())#, required=True,) # maybe not include required=True"
	'''def __init__(self, *args, **kwargs):
		super(dbForm, self).__init__(*args, **kwargs)
		self.fields['model_classes_field'] = forms.ChoiceField(
            choices=models() )
	'''
#class dbForm(forms.Form):
	#model_classes_field = forms.ModelChoiceField(queryset=Attributes.objects.all(), required=True,)
	
class editForm(forms.Form):
	field = forms.CharField()

#class editForm(forms.Form):
	#model_fields = forms.ChoiceField()

#ModelForm test
def get_form(type_id):
	ctype = ContentType.objects.get(pk=type_id)
	model_class = ctype.model_class()
	class ObjForm(forms.ModelForm ):
	    class Meta:
	        model = model_class
		def __init__(self, *args, **kwargs):
			model_classes_field = forms.ChoiceField(choices=models(), required=True,)
	return ObjForm

''' all possible model forms
class AttributesForm(forms.ModelForm):   
class EmployeesForm(forms.ModelForm):   
class DepartmentForm(forms.ModelForm):  
class InstructorsForm(forms.ModelForm):    
class KatefthForm(forms.ModelForm):
class KatefthKykloiForm(forms.ModelForm):    
class KykloiForm(forms.ModelForm):   
class KykloiExaminaForm(forms.ModelForm):    
class ModuleKykloiForm(forms.ModelForm):
class ModulesForm(forms.ModelForm):    
class ModulesTutorsForm(forms.ModelForm):   
class PubInstrForm(forms.ModelForm):   
class PubTypesForm(forms.ModelForm):    
class PublicationsForm(forms.ModelForm ):    
class RanksForm(forms.ModelForm):    
class ServiceForm(forms.ModelForm ):
class UsersForm(forms.ModelForm):   
class WorksForm(models.Model):
'''

