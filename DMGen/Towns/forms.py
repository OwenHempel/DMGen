# class GeneratorForm(forms.Form):
# 	'''A simple form to enter an Octal or decimal filter value'''
# 	self.Info = {}
# 	def __init__(self, *args, **kwargs):
# 		super(PlotForm, self).__init__(*args, **kwargs)
# 		self.Info = kwargs
from django.apps import apps
from django import forms
from .models import Town
ModelList = apps.all_models['Towns']

class TownForm(forms.ModelForm):
	class Meta:
		model = Town
		fields = ['Name', 'Shops', 'Residents']


# class GenerateForm(forms.ModelForm):
# 	class Meta:
# 		model = self.model