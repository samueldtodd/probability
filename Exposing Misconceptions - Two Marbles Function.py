# Brilliant - Exposing Misconceptions from Perplexing Probabilities
# Set up
# Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag.
# if the coin is tails, a blue marble is put into the bag. You pick out a marble at random. It's red. You place it back
# into the bag. What is the chance that next time you pull out a blue marble?

# The answer is 0.25. The purpose of this function is prove this result by simulating this game a large number of times

def calc_probability(number_of_games):

	import random

	per_game = [] 
	final_marble = []
	blue = ['Blue', 'Blue']

	# Simulate the number of tries
	for game in range(0, number_of_games): 

		bag = []
		# Simulate the coin flip and combination of marbels placed into the bag
		for marbles in range(0,2):

			flip = random.randint(0,1)

			if flip == 0:
				bag.append("Red")
			else:
				bag.append("Blue")

		per_game.append(bag)

	for selection in per_game:
		# Disregard marble combination Blue, Blue as irrelevant to the set up
		if selection != blue:
			
			# Simulate removing a marble at random
			selected_marble = random.choice(selection)
			
			# We only want results where Red is the first chosen marble
			if selected_marble == "Red":
				
				# Simulate returning the Red marble and choosing another at random
				random_marble = random.choice(selection)
				
				# Appending this chosen marble to a list
				final_marble.append(random_marble)
		
			elif selected_marble == "Blue":
				pass
		
		else:
			pass

	# Calculating the probability of the marbel being blue
	print("Odds of Blue: " +str(1 - final_marble.count("Red") / len(final_marble)))