import random

results = []

for roll in range(0, 100000):
	dice_one = random.randint(1,6)
	dice_two = random.randint(1,6)
	if (dice_one > 4) | (dice_two > 4):
		results.append('Lose')
	else:
		results.append('Win')


print(results.count('Win') / (results.count('Lose') + results.count('Win')))

