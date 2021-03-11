#Brilliant - Exposing Miconceptions from Perplexing Probability
#Set Up
#Two people are playing a game. They each take turns to flip their own coin. If the flips match, they flip again. The games ends when the two flips don't match. If it's HT, 
#Player 1 wins, if it's TH Player 2 wins. If this game is played with weighted coins that land on heads 99% of time and tails 1% of the time, is the game fair?

#The answer is yes, the game is fair. Over a large number of games, both players have an equal change of winning

def test_fairness(number_of_simulations):

	ending_outcomes = []
	player_1_win_condition = ['Heads', 'Tails']

	import random

	for game in range(0,1000):
		
		game_result = ['Heads', 'Heads']

		while game_result == ['Heads', 'Heads'] or game_result == ['Tails', 'Tails']:

			coin_1 = random.randint(0,100)
			coin_2 = random.randint(0,100)

			if coin_1 > 0 and coin_2 > 0:
				game_result = ['Heads', 'Heads']
			
			elif coin_1 == 0 and coin_2 > 0:
				game_result = ['Tails', 'Heads']
			
			elif coin_1 > 0 and coin_2 == 0:
				game_result = ['Heads', 'Tails']
			
			else:
				game_result = ['Tails', 'Tails']

		ending_outcomes.append(game_result)

	player_1_wins = 0
	player_2_wins = 0

	for outcome in ending_outcomes:
		if outcome == player_1_win_condition:
			player_1_wins += 1
		else:
			player_2_wins += 1

	print('After ' + str(number_of_simulations) + ' simulations, Player 1 won with a probability of ' + str(player_1_wins/(player_1_wins + player_2_wins)) + ' and Player 2 won with a probability of ' + str(1-(player_1_wins/(player_1_wins + player_2_wins))) + '. After a sufficiently high number of simulations, no player has a distinct advantage, therefore the game is fair.')

print("Two people are playing a game. They each take turns to flip their own coin. If the flips match, they flip again. The games ends when the two flips don't match. Player 1 wins if the result is HT, Player 2 ins if the result is TH. If this game is played with weighted coins that land on heads 99% of time and tails 1% of the time, is the game fair?")

print("How many games would you like to simulate?")

number_of_simulations = int(input())

test_fairness(number_of_simulations)


