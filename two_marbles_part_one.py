# Brilliant - Exposing Misconceptions from Perplexing Probabilities
# Set up
# Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag.
# If the coin is tails, a blue marble is put into the bag. You pick out a marble at random. It's red. You place it back
# into the bag. What is the chance that next time you pull out a blue marble?

# The answer is 0.25. The purpose of this function is prove this result by simulating this game a large number of times

import random

def check_input(input_value):
	while input_value != int:    
		try:
			input_value = int(input_value)
		except ValueError:
			input_value = input('An integer must be entered. Try again: ')
			input_value = check_input(input_value)
        
		try:
			if input_value <= 0:
				input_value = input('Value must be greater than 0. Try again: ')
				input_value = check_input(input_value)

		except:
			input_value = check_input(input_value)
            
		return input_value

def calc_probability(simulations):

	per_game = [] 
	final_marble = []
	blue = ['Blue', 'Blue']

	# Simulate the number of games
	for game in range(0, simulations): 

		bag = []
		# Simulate the coin flip and combination of marbles placed into the bag
		for marbles in range(0,2):

			flip = random.randint(0,1)

			if flip == 0:
				bag.append("Red")
			else:
				bag.append("Blue")

		per_game.append(bag)

	for selection in per_game:
		# Disregard marble combination Blue, Blue as irrelevant to set up
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

	final_probability = round(1-final_marble.count("Red") / len(final_marble),3)		

	# Calculating the probability of the marble being blue
	print(f"After simulating {str(simulations)} games, a blue marble was pulled out with probability of {str(final_probability)}. The actual probability of a blue marble being pulled out is 0.25")

print("""Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag. If the coin is tails, a blue marble is put into the bag. You pick out a marble at random. It's red. You place it back into the bag. What is the chance that next time you pull out a blue marble?""")

simulations = input("How many games would you like to simulate? ")
simulations = check_input(simulations)

calc_probability(simulations)