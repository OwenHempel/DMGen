from django.db import models

# Create your models here.
class Race(models.Model):
	RaceText = models.CharField(max_length = 15)

class Age(models.Model):
	AgeText = models.CharField(max_length = 10)

class Gender(models.Model):
	GenderText = models.CharField(max_length = 10)

class Name(models.Model):
	NameText = models.CharField(max_length = 25)
	Race = models.ForeignKey(Race)
	Gender = models.ForeignKey(Gender)
	Position = models.IntegerField(default = 0)

class Appearance(models.Model):
	AppearanceText = models.CharField(max_length =25)
	Probability = models.IntegerField(default = 0)

class Personality(models.Model):
	PersonalityText = models.CharField(max_length = 25)
	Probability = models.IntegerField(default = 0)

class NPC(models.Model):
	FirstName = models.ForeignKey(Name)
	LastName = models.ForeignKey(Name)
	Race = models.ForeignKey (Race)
	Gender = models.ForeignKey(Gender)
	Age = models.ForeignKey(Age)
	Appearance = models.ManyToManyField(Appearance)
	Personality = models.ManyToManyField(Personality)

class ShopType(models.Model):
	Type = models.CharField(max_length = 15)

class ShopName(models.Model):
	Type = models.ForeignKey(ShopType)
	Position = models.IntegerField(default = 0)
	NameText = models.CharField(max_length = 15)

class ItemType(models.Model):
	Type = models.CharField(max_length = 15)

class ItemEffect(models.Model):
	Name1 = models.CharField(max_length = 15)
	Name2 = models.CharField(max_length = 15)
	Effect = models.CharField(max_length = 100)
	Type = models.ForeignKey(ItemType)

class Item(models.Model):
	Name = models.CharField(max_length = 40)
	Cost = models.IntegerField(default = 0)
	Notes = models.CharField(max_length = 100)
	Type = models.ForeignKey(ItemType)
	Effect = models.ManyToManyField(ItemEffect)
	Attunement = models.BooleanField(default = False)
	Rarity = models.CharField(max_length = 15)

class Shop(models.Model):
	Owner = ForeignKey(NPC)
	Balance = models.IntegerField(default = 0)
	Inventory = models.ManyToManyField(Item)
	Name = models.CharField(max_length = 40)

class Town(models.Model):
	Shops = models.ManyToOneField(Shop)
	Residents = models.ManyToOneField(NPC)
	