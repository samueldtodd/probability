#How many people must be gathered together in a room, before you can be certain 
#that there is a greater than 50/50 chance that at least two of them have the same birthday?

import random
import statistics

def birthday_simulation(simulation_amount):
	
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

print('''You are alone in a room. One by one a new person will enter and share their birthday with the group. On average, how many people need to enter the room before there is a greater than 50/50 chance that two share a birthday? This code simulates this event a set number of times and returns the median number of people who entered the room before two shared a birthday.''')

birthday_simulation(1000)


