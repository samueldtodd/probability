#Perplexing Probability - Russian Roulette
#Setup
#In standard Russian Roulette there are 6 players and 1 revolver. The revolver has a
#cylinder with 6 chambers. Initially, all 6 chambers are empty. The game starts when 
#one of the players inserts a bullet into one of the chambers and then spins the 
#cylinder so that a random chamber is in the pistol's firing position. Each turn, the
#player with the gun points it at their own head and pulls the trigger. If the 
#chamber with the bullet is in the firing position, the player is shot. If not, 
#the cylinder rotates so that the next chamber in the circular arrangement is in 
#the firing position. The player passes the revolver to the next player and the 
#process is repeated until everyone has had a turn. If there is only 1 
#bullet in the gun, then the game effectively ends when a person is shot.
#Are your chances of winning Russian Roulette (by surviving) better if you're the 
#first player to shoot, the last player to shoot, or some player in the middle of 
#the game?

import random

def check_input(input_value, maximum):
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


def roulette(games):

	players = {'Player 1': 0, 'Player 2': 0, 'Player 3':0, 'Player 4':0, 'Player 5':0, 'Player 6':0}

	for games in range(games):
		chamber_position = [1, 2, 3, 4, 5, 6]
		for key in players:
			
			bullet_position = random.choice(chamber_position)
			chamber_position.remove(bullet_position)

			if bullet_position == 1:
				players[key] += 1
			else:
				players[key] += 0

	print("Afer " + str(games+1) + " rounds the players survived with the following probabilities:")
	s = sum(players.values())
	for k, v in players.items():
	    pct = v / s
	print(k,":",1 - pct)

print('''You are playing a standard game of Russian Roulette. The revolver has six cylinders and there are six players. One bullet is placed in the cylinder and is spun to a random position. The cylinder is not spun again. The players take turns to fire the revolver. The game ends when the bullet is fired. Are your chances of winning (by surviving) better if you're the first (Player 1) player to shoot, the last player to shoot (Player 6), or some player in the middle of the game (Players 2-5)?''')

player = input('Which position would you like to go in to give you best chance of survival? (1-6): ')

player = check_input(player)

games = int(input('How many rounds would you like to simulate?'))

roulette(games)

print("It does matter in which order you shoot as the odds of survival are the same. As the number of rounds increase, the probabilities will converge to 0.1666")

