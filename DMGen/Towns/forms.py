

from django import forms
from .models import Town, NPC, Shop, Item

class TownForm(forms.ModelForm):
	class Meta:
		model = Town
		fields = ['Name', 'Shops', 'Residents']

class NPCForm(forms.ModelForm):
	class Meta:
		model = NPC
		fields = ['FirstName', 'LastName', 'Race', 'Gender', 'Appearance', 'Age', 'Personality']

class ShopForm(forms.ModelForm):
	class Meta:
		model = Shop
		fields = ['FirstName', 'LastName', 'Owner', 'Inventory', 'Balance', 'Type']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['Name', 'Cost', 'Type', 'Effect']