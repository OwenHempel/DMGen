from django.db import models

# Create your models here.
class Race(models.Model):
	RaceText = models.CharField(max_length = 15)
	def __str__(self):
		return self.RaceText

class Age(models.Model):
	AgeText = models.CharField(max_length = 30)
	def __str__(self):
		return self.AgeText

class Gender(models.Model):
	GenderText = models.CharField(max_length = 10)
	def __str__(self):
		return self.GenderText

class Name(models.Model):
	NameText = models.CharField(max_length = 25)
	Race = models.ForeignKey(Race, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Gender = models.ForeignKey(Gender, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Position = models.IntegerField(default = 0)
	def __str__(self):
		return "{}, {} {} ({})".format(self.NameText, self.Race, self.Gender, self.Position)

class Appearance(models.Model):
	AppearanceText = models.CharField(max_length =25)
	Probability = models.IntegerField(default = 0)
	def __str__(self):
		return self.AppearanceText

class Personality(models.Model):
	PersonalityText = models.CharField(max_length = 25)
	Probability = models.IntegerField(default = 0)
	def __str__(self):
		return self.PersonalityText

class NPC(models.Model):
	FirstName = models.ForeignKey(Name, related_name = 'FirstName', blank = True, default = '', on_delete = models.SET_DEFAULT)
	LastName = models.ForeignKey(Name, related_name = 'LastName', blank = True, default = '', on_delete = models.SET_DEFAULT)
	Race = models.ForeignKey(Race, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Gender = models.ForeignKey(Gender, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Age = models.ForeignKey(Age, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Appearance = models.ManyToManyField(Appearance)
	Personality = models.ManyToManyField(Personality)

class ShopType(models.Model):
	Type = models.CharField(max_length = 15)
	def __str__(self):
		return self.Type

class ShopName(models.Model):
	Type = models.ForeignKey(ShopType, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Position = models.IntegerField(default = 0)
	NameText = models.CharField(max_length = 25)
	def __str__(self):
		return "{}, {} ({})".format(self.Type, self.NameText, self.Position)

class ItemType(models.Model):
	Type = models.CharField(max_length = 30)
	Slot = models.CharField(max_length = 10)
	def __str__(self):
		return "{}, {}".format(self.Type, self.Slot)

class ItemEffect(models.Model):
	Name1 = models.CharField(max_length = 15)
	Name2 = models.CharField(max_length = 15)
	Effect = models.CharField(max_length = 410)
	Type = models.ManyToManyField(ItemType)
	def __str__(self):
		return "{}, {}: {}".format(self.Name1, self.Name2, self.Effect)	

class Item(models.Model):
	Name = models.CharField(max_length = 40)
	Cost = models.IntegerField(default = 0)
	Notes = models.CharField(max_length = 100)
	Type = models.ForeignKey(ItemType, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Effect = models.ManyToManyField(ItemEffect)
	Attunement = models.BooleanField(default = False)
	Rarity = models.CharField(max_length = 15)

class Shop(models.Model):
	Owner = models.ForeignKey(NPC, blank = True, default = '', on_delete = models.SET_DEFAULT)
	Balance = models.IntegerField(default = 0)
	Inventory = models.ManyToManyField(Item)
	FirstName = models.ForeignKey(ShopName, related_name = 'FirstName', blank = True, default = '', on_delete = models.SET_DEFAULT)
	LastName = models.ForeignKey(ShopName, related_name = 'LastName', blank = True, default = '', on_delete = models.SET_DEFAULT)

class Town(models.Model):
	Shops = models.ManyToManyField(Shop)
	Residents = models.ManyToManyField(NPC)
	