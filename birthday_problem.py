import random
import statistics

probability = []
lengths = []

for simulations in range(0, 100):
	birthdays = []
	for people in range(0,365):
		birthday = random.randint(0,365)
		if birthday not in birthdays:
			birthdays.append(birthday)
		else:
			birthdays.append(birthday)
			lengths.append(len(birthdays))
			break

print(lengths)		

