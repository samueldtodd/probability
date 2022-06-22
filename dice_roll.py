import random

class Die():

	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		roll = random.randint(1, self.sides)
		return roll

win = 0.0
lose = 0.0

d1 = Die()
d2 = Die()

for roll in range(0, 100000):

	d1r = d1.roll_die()
	d2r = d2.roll_die()

	if (d1r > 4) | (d2r > 4):
		lose += 1
	else:
		win += 1

print(win / (win + lose))

print(4.0/6) * (4.0/6)

