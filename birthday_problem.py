#How many people must be gathered together in a room, before you can be certain 
#that there is a greater than 50/50 chance that at least two of them have the same birthday?

import random
import statistics

simulation_amount = 100000
lengths = []

for simulations in range(0, simulation_amount):
	birthdays = []
	for people in range(0,365):
		birthday = random.randint(0,365)
		if birthday not in birthdays:
			birthdays.append(birthday)
		else:
			birthdays.append(birthday)
			lengths.append(len(birthdays))
			break

print("After", simulation_amount, "simulations, an average of", (statistics.median(lengths)), "people entered the room before two shared a birthday.")