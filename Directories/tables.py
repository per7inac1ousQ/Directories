import django_tables2 as tables
from django.db.models import get_models, get_app, get_model

#create a ModelForm using a dynamic model
def get_table(c_model):
	model_class = get_model('Directories', c_model)	
	class ObjTable(tables.Table):
		selection = tables.CheckBoxColumn(accessor='pk')
		class Meta:
			model = model_class
			sequence = ("selection", "...")
			attrs = {"class": "mod_table"}
	return ObjTable
