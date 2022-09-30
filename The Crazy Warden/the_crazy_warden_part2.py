def check_input(input_value, max, colour):

    while input_value != int:
        
        try:
            input_value = int(input_value)
        except ValueError:
            input_value = input("A number must be entered. Try again: ")
            input_value = check_input(input_value, max, colour)        
        try: 
            if input_value > max:
                input_value = input(f"You have {max} {colour} pills remaining. Enter a lower amount: ")
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

def crazy_warden_two_desc():
    print('Impressed with your strategy yesterday the warden gives you a choice: you can either have one extra bottle to distribute pills into (giving you three bottles) OR you can have 25 extra white pills. Given one of these options, you’ll play essentially the same game: first you’ll distribute the pills, then, blindfolded, you’ll choose a bottle and then take a random pill from it; if you pick a white pill, you live, and if you pick a black pill, you die.')
    print('\n')
    print('Given these options, which solution provides the highest possibility of survival?')
    crazy_warden_two()

def crazy_warden_two():
    print('\n')
    print('Which offer would you like to accept?: ')
    print('\n')
    print('A) Take the extra bottle')
    print('B) Take the extra 25 pills')
    selection = input('Enter A or B: ' ).upper()

    while (selection != 'A') and (selection != 'B'):
        selection = input('Enter A or B: ' ).upper()

    if selection == 'A':
        crazy_warden_two_a()
    elif selection == 'B':
        crazy_warden_two_b()

def crazy_warden_two_a():

    bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")         
    bt1_w = check_input(bt1_w, 50, 'WHITE')

    bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")         
    bt1_b = check_input(bt1_b, 50, 'BLACK')

    while ((bt1_w == 0) & (bt1_b == 0)) or ((bt1_w == 50) & (bt1_b == 50)) or (bt1_w + bt1_b >= 99):
            print("Each bottle must contain at least one pill, please select again")
            bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")
            bt1_w = check_input(bt1_w, 50, 'WHITE')
            
            bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")
            bt1_b = check_input(bt1_b, 50, 'BLACK')

    print(f'You have {50-bt1_w} WHITE pills remaining, and {50-bt1_b} BLACK pills remaining')
    print('\n')
    bt2_w = input('How many WHITE pills would like to put in bottle two?: ')
    bt2_w = check_input(bt2_w, 50-bt1_w, 'WHITE')

    bt2_b = input('How many BLACK pills would like to put in bottle two?: ')
    bt2_b = check_input(bt2_b, 50-bt1_b, 'BLACK')

    while ((bt2_w == 0) & (bt2_b == 0)) or ((bt1_b == 50-bt1_w) & (bt2_b == 50-bt2_b)) or (((50 - bt1_w - bt2_w) + (50 - bt1_b - bt2_b)) <= 1):
            print("Each bottle must contain at least one pill, please select again")
            bt2_w = input("How many WHITE pills would you like to put in bottle two?: ")
            bt2_w = check_input(bt2_w, 50-bt1_w, 'WHITE')
            
            bt2_b = input("How many BLACK pills would you like to put in bottle two?: ")
            bt2_b = check_input(bt2_b, 50-bt1_b, 'BLACK')

    bt3_w = 50 - bt1_w - bt2_w
    bt3_b = 50 - bt1_b - bt2_b

    print(f"Bottle 1 contains {bt1_w} white pills and {bt1_b} black pills")
    print(f"Bottle 2 contains {bt2_w} white pills and {bt2_b} black pills")
    print(f"Bottle 3 contains {bt3_w} white pills and {bt3_b} black pills")
    print('\n')

    probability_a = round(((1/3) * bt1_w/(bt1_w + bt1_b)) + (1/3) * (bt2_w/(bt2_w + bt2_b))+ (1/3) * (bt3_w/(bt3_w + bt3_b)), 3)
    
    print(f'If you were to select a bottle and a pill at random, your probability of survival would be {probability_a}')
    print('\n')

    if probability_a == 0.83:
        print('This is your overal best chance of survival!')
        print('\n')
        again_input = input('Would you like to move onto the final test? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to move onto the final test? (yes/no): ')
        
        if again_input == 'yes':
            from the_crazy_warden_part3 import crazy_warden_three_desc
        else:
            quit()

    elif probability_a < 0.83:
        again_input = input('This is not your best chance of survival, would you like try again? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to try again? (yes/no): ')
        
        if again_input == 'yes':
            crazy_warden_two()
        else:
            quit()

def crazy_warden_two_b():

    print('\n')
    print('The warden gives you an extra 25 pills, you now have 75 WHITE pills and 50 BLACK pills.')
    print('\n')
    bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")         
    bt1_w = check_input(bt1_w, 75, 'WHITE')

    bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")         
    bt1_b = check_input(bt1_b, 50, 'BLACK')

    while ((bt1_w == 0) & (bt1_b == 0)) or ((bt1_w == 75) & (bt1_b == 50)):
        print("Each bottle must contain at least one pill, please select again")
        bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")
        bt1_w = check_input(bt1_w, 75, 'WHITE')
        
        bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")
        bt1_b = check_input(bt1_b, 50, 'BLACK')

    print('\n')
    print(f"Bottle 1 contains {bt1_w} white pills and {bt1_b} black pills")
    print(f"Bottle 2 contains {75 - bt1_w} white pills and {50 - bt1_b} black pills")
    print('\n')
    
    confirm = input('Are you happy with this selection? (yes/no): ')
    while (confirm != 'yes') and (confirm != 'no'):
        confirm = input('Are you happy with this selection? (yes/no): ')

    if confirm == 'no':
        crazy_warden_two_b()

    bt2_w = 75-bt1_w
    bt2_b = 50-bt1_b

    probability = round((0.5 * bt1_w/(bt1_w + bt1_b)) + 0.5 * (bt2_w/(bt2_w + bt2_b)),3)

    print('\n')
    print(f'If you were to select a bottle and a pill at random, your probability of survival would be {probability}')
    print('\n')
    
    if probability == 0.798:
        print('This is your best chance of survival if you accept the additonal WHITE pills. However, it is not your best chance of survival overall.')
        print('\n')
        again_input = input('Would you like to try again? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to try again? (yes/no): ')
        
        if again_input == 'yes':
            crazy_warden_two()
        else:
            quit()

    elif probability < 0.798:
        again_input = input('This is not your best chance of survival, would you like try again? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to try again? (yes/no): ')
        if again_input == 'yes':
            crazy_warden_two()
        else:
            quit()

crazy_warden_two_desc()