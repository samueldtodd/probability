#You're offered the following bet: two dice will be rolled simultaneously, if neither
#die show a 5 or 6 you win. If either die shows 5 or 6, you lose. It's a good bet if the odds of winning are greater than 50%.
#Should you take the bet? 

import random

#function to check input is an integer greater than 0
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

#create Die class
class Die():

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1, self.sides)
        return roll


def run_sims(simulations):
#Simulate rolls 

    #Create two instances of Die class
    d1 = Die()
    d2 = Die()

    win = 0.0
    lose = 0.0

    for roll in range(0, simulations):


        d1r = d1.roll_die()
        d2r = d2.roll_die()

        if (d1r > 4) | (d2r > 4):
            lose += 1
        else:
            win += 1
            
    result = round(win / (win+lose),4)
    return result

#Show results
def results(result):
    if result >= 0.5 and has_bet == 'y':
        print(f'''You beat the odds! After {simulations} games you won {result} of games. 
The odds of winning each game were 0.444. Try running a greater number of simulations and see if your luck continues.\n''')
    elif result >= 0.5 and has_bet == 'n':
        print(f'''You beat the odds and but did not bet! However, you were correct not to take it. After {simulations} games you won {result} of games.
The odds of winning each game were 0.444. Try running a greater number of simulations and see if your luck continues.\n''')
    elif result <= 0.5 and has_bet == 'n':
        print(f'You were right not to take the bet! After {simulations} games, you won {result} of games. The odds were less than 0.5 and therefore not in your favour. The actual odds of winning are 0.444.\n')
    elif result <0.5 and has_bet == 'y':
        print(f'You should not have taken the bet! After {simulations} games, you won {result} of games. The odds were less than 0.5 and therefore not in your favour. The actual odds of winning are 0.444\n')

#Give an explanation if the user requests it
def give_explanation():
    print('''There are four potential outcomes of the dice roll:\n
    1. Both die show 5 or 6
    2. Die One shows 5 or 6, Die Two shows 1, 2, 3, 4
    3. Die Two shows 5 or 6, Die One shows 1, 2, 3, 4
    4. Both die show 1, 2, 3, 4\n
In the event of outcomes 1-3 occurring, you lose. You only win if outcome 4 occurs, therefore the odds of winning
are the same as the odds of outcome 4 occurring. As the dice rolls are independent (the outcome of one does not
impact the other), the total odds are found by multiplying together the odds that each individual die shows 1, 2, 3, 4.
The odds of rolling 1, 2, 3, 4 on a 6-sided die are 4/6. Therefore the final odds are (4/6) * (4/6): 0.444\n''')
    

#Ask if the player would take the bet
def bet():
    
    print('''You're offered the following bet: two dice will be rolled simultaneously, if neither
die show a 5 or 6 you win. If either die shows 5 or 6, you lose. It's a good bet if the odds of winning are greater 
than 50%.\n''')
    
    bet = input('Should you take the bet? (y/n) ')

    while (bet.lower() != 'y') and (bet.lower() != 'n'):
        bet = input('Should you take the bet? (y/n) ')
        
    return bet

#Check with the player wants to play again
def play_again():
    
    again = input('Would you like to run the simulation again? (y/n) ')
    
    while (again.lower() != 'y') and (again.lower() != 'n'):
        
        again = input('Would you like to run the simulation again? (y/n) ')
        
    return again

#Game loop
play = True

while play == True:
    has_bet = bet()
    
    if has_bet == 'y':
        print('You have taken the bet! Lets simulate some rounds.\n')
    elif has_bet == 'n':
        print('You have not taken the bet! Let simulate some rounds.\n')
    
    simulations = input('How many simulations would you like to run? ')
    simulations = check_input(simulations)
    print('\n')
    result = run_sims(simulations)
    results(result)
    
    explanation = input('Would you like an explanation? (y/n) ')
    
    while (explanation.lower() != 'y') and (explanation.lower() != 'n'):
        explanation = input('Would you like an explanation (y/n) ')
        
    if explanation == 'y':
        print('\n')
        give_explanation()
        again = play_again()
    
    elif explanation == 'n':
        again = play_again()
        
    if again == 'y':
        continue
    elif again == 'n':
        play = False