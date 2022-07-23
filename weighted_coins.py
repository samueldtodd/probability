#Taken from Brilliant.org - Exposing Miconceptions from Perplexing Probability
#Set Up
#Two people are playing a game. They each take turns to flip their own coin. If the flips match, they flip again. 
#The game ends when the two flips don't match, in which case the Player who flipped heads is the winner. 
#If this game is played with weighted coins that land on heads 99% of time and tails 1% of the time, is the game fair?

#The answer is yes, the game is fair. Over a large number of games, both players have an equal change of winning

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

def test_fairness(simulations):

	player_1_wins = 0
	player_2_wins = 0

	for game in range(0,simulations):
		
		play = True

		while play == True:

			coin_1 = random.randint(0,100)
			coin_2 = random.randint(0,100)

			if coin_1 > 0 and coin_2 > 0:
				pass
			
			elif coin_1 > 0 and coin_2 == 0:
				player_1_wins += 1
				play = False
			
			elif coin_1 == 0 and coin_2 > 0:
				player_2_wins += 1
				play = False
			
			else:
				pass

	print('After ' + str(simulations) + ' simulations, Player 1 won with a probability of ' + str(round(player_1_wins/(player_1_wins + player_2_wins),4)) + ' and Player 2 won with a probability of ' + str(round(1-(player_1_wins/(player_1_wins + player_2_wins)),4)) + ". The more simulations that are run, the closer each player's probability of winning approaches 0.5, therefore the game is fair.")

print("Two people are playing a game. They each take turns to flip their own coin. If the flips match, they flip again. The game ends when the two flips don't match, in which case the player with heads is the winner. If this game is played with weighted coins that land on heads 99% of time and tails 1% of the time, is the game fair?\n")

simulations = input("How many games would you like to simulate? ")
print('\n')
simulations = check_input(simulations)

test_fairness(simulations)