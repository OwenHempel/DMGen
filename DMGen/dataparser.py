with open ("log.txt", 'w') as log:
	filename = input("Enter File Name:")
	with open(filename, 'r') as f:
		for line in f:
			l = line.split(',')
			header = l[0].split(' ')
			race = Race.objects.get(RaceText = header[0])
			if header[1] == 'Last':
				position = 2
				gender = Gender.objects.get(GenderText = 'Genderless')
			else:
				gender = Gender.objects.get(GenderText = header[1])
				position = 1
			l.pop(0)
			l = [x for x in l if x != '']
			print (header, len(l))
			for i in l:
				ie = Name(Race = race, Gender = gender, Position = position, NameText = i)
				ie.save()