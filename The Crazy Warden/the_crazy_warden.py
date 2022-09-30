import random

def check_input(input_value, max, colour):

    while input_value != int:
        
        try:
            input_value = int(input_value)
        except ValueError:
            input_value = input("A number must be entered. Try again: ")
            input_value = check_input(input_value, max, colour)        
        try: 
            if input_value > max:
                input_value = input(f"You only have {max} {colour} pills remaining. Enter a lower amount: ")
                input_value = check_input(input_value, max, colour)
            elif input_value < 0:
                input_value = input("The amount can't be negative. Try again: ")
                input_value = check_input(input_value, max, colour)
        except ValueError:
            input_value = input("A number must be entered Try again: ")
            input_value = check_input(input_value, max, colour)
        except TypeError:
            input_value = input("Enter a number: ")
            input_value = check_input(input_value, max, colour)

        return input_value

def try_again(response):
    while (response != 'yes') and (response != 'no'):
        response = input('Would you like to try again? (yes/no): ')
    print('\n')
    return response

def crazy_warden_one_desc():
    print('\n')
    print('You are a prisoner sentenced to death. The warden offers you an opportunity to live if you can win at the following game of chance. He gives you a bottle of 50 white pills and an identical bottle of 50 black pills that are the same size and shape as the white pills.')
    print('\n')
    print('He then says, "You can split up these pills however you want among these two bottles, so long as you use all the pills and leave at least one pill in each bottle. In five minutes, I will blindfold you and put the two bottles you’ve made in front of you in a random order and shaken so that the pills you placed in each bottle get mixed around. You will then choose one bottle at random and then take (and eat) one pill from it. If the pill is white you will live to see another day, but if the pill is black... you will die.')
    print('\n')
    print('If you’re as clever as you can be about how you divide the 100 pills into bottles, what is the highest probability of choosing a white pill that can be achieved?')
    print('\n')
    crazy_warden_one()

def crazy_warden_one():

    bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")         
    bt1_w = check_input(bt1_w, 50, 'WHITE')

    bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")
    bt1_b = check_input(bt1_b, 50, 'BLACK')

    while ((bt1_w == 0) & (bt1_b == 0)) or ((bt1_w == 50) & (bt1_b == 50)):
        print("Each bottle must contain at least one pill, please select again")
        bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")
        bt1_w = check_input(bt1_w, 50, 'WHITE')

        bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")
        bt1_b = check_input(bt1_b, 50, 'BLACK')

    print('\n')
    print(f"Bottle 1 contains {bt1_w} WHITE pills and {bt1_b} BLACK pills")
    print(f"Bottle 2 contains {50 - bt1_w} WHITE pills and {50 - bt1_b} BLACK pills")
    print('\n')
    confirm = input('Are you happy with this selection? (yes/no): ')
    while (confirm != 'yes') and (confirm != 'no'):
        confirm = input('Are you happy with this selection? (yes/no): ')

    if confirm == 'no':
        crazy_warden_one()

    bt2_w = 50-bt1_w
    bt2_b = 50-bt1_b

    probability = round((0.5 * bt1_w/(bt1_w + bt1_b)) + 0.5 * (bt2_w/(bt2_w + bt2_b)),3)

    print(f'If you were to select a bottle and a pill at random, your probability of survival would be {probability}')

    print('\n')
    if probability != 0.747:
        response = input('Good try! But this can be improved. Would you like to try again? (yes/no) ')
        
        response = try_again(response)
        
        if response == 'yes':
            crazy_warden_one()
        elif response == 'no':
            quit
    
    elif probability == 0.747:
        response = input('Congratulations! This combination gives the highest probability of choosing a white pill! Would you like to move onto the next test? (yes/no): ')
        response = try_again(response)

        if response == 'yes':
            from the_crazy_warden_part2 import crazy_warden_two_desc
        elif response == 'no':
            quit

crazy_warden_one_desc()