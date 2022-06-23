# Brilliant - Exposing Misconceptions from Perplexing Probabilities
# Set up
# Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag.
# If the coin is tails, a blue marble is put into the bag. You look into the bag and see at least one of the marbles is red.
# A red marble is set aside. What is the probability the remaining marble is blue?

# The answer is 0.66. The purpose of this function is to prove this result by simulating this game a user-specified number
# of times and printing the result

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
	remaining_marble = []
	both_blue = ['Blue', 'Blue']

	#Simulate the number of games
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

	for game in per_game:

		# Disregard marble combination Blue, Blue as irrelevant to the set up
		if game != both_blue:

			#Remove a single red marble from each bag to simulate setting it aside
			game.remove('Red')

			#Create a bag for the single remaining marble
			remaining_marble.append(game)

	Blue = 0
	Red = 0

	#Count the colour of the remaining marble per game
	for result in remaining_marble:
		for marble in result:
			if marble == 'Blue':
				Blue += 1
			else:
				Red += 1

	final_probability = round(Blue/(Blue+Red),3)			

	#Calculate the probability of the remaining marble being Blue			
	print('After simulating ' + str(simulations) + ' games, the probability of the remaining marble being blue is: ' + str(final_probability))

print("""Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag. If the coin is tails, a blue marble is put into the bag. You look into the bag and see at least one of the marbles is red. A red marble is set aside. What are the odds the remaining marble is blue?""")

simulations = input("How many games would you like to simulate? ")
simulations = check_input(simulations)

calc_probability(simulations)
