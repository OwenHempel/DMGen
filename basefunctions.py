import random

def roll_die(faces):
	return random.randint(1,faces)

def roll_dice(n, faces):
	'''Returns a list of n rolls of f-sided dice. 
	Usage: rolls = roll_dice(n,f)'''
	rolls = []
	for i in range(n):
		rolls.append(roll_die(faces))
	return rolls

