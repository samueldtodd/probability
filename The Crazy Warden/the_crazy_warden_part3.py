def check_input(input_value, max):

    while input_value != int:
        
        try:
            input_value = int(input_value)
        except ValueError:
            input_value = input("A number must be entered. Try again: ")
            input_value = check_input(input_value, max)        
        try: 
            if input_value > max or input_value < 0:
                input_value = input(f"Enter a number between 0 and {max}: ")
                input_value = check_input(input_value, max)
        except ValueError:
            input_value = input("A number must be entered Try again: ")
            input_value = check_input(input_value, max)
        except TypeError:
            input_value = input("Enter a number: ")
            input_value = check_input(input_value, max)

        return input_value

def crazy_warden_three_desc():
    print("As you have survived the first two tests, the warden offers one final test. The warden offers you a new setup: 3 bottles, 30 red pills, 30 black pills, and 30 white pills.")
    print("\n")
    print('The red pills and the black pills are both poisonous on their own, but neutralize each other if taken together. The white pills are still harmless. He says: "This time, when I blindfold you and mix up the bottles, you’ll randomly choose two bottles of the three you prepare and pick one pill from each of those two bottles. The combinations red-black and white-white will allow you to live, but take any other combination (black-black, red-red, white-black, or white-red) and you’ll die. Again, you can distribute the pills however you want, so long as you use all of them and put at least one pill in each bottle.')
    print("\n")
    print('How would you divide the pills to give the best chance of survival?')
    print('\n')
    crazy_warden_three()

def crazy_warden_three():
    print('\n')
    print("You have 30 WHITE pills, 30 BLACK pills and 30 RED pills.")
    print("\n")
    bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")         
    bt1_w = check_input(bt1_w, 30)

    bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")         
    bt1_b = check_input(bt1_b, 30)

    bt1_r = input("How many RED pills would you like to put in bottle one?: ")         
    bt1_r = check_input(bt1_r, 30)

    while ((bt1_w == 0) & (bt1_b == 0) & (bt1_r == 0)) or ((bt1_w == 30) & (bt1_b == 30) & (bt1_r == 30)) or (bt1_w + bt1_b + bt1_r > 88):
        print("Each bottle must contain at least one pill, please select again")
        bt1_w = input("How many WHITE pills would you like to put in bottle one?: ")
        bt1_w = check_input(bt1_w, 30)
        
        bt1_b = input("How many BLACK pills would you like to put in bottle one?: ")
        bt1_b = check_input(bt1_b, 30)

        bt1_r = input("How many RED pills would you like to put in bottle one?: ")         
        bt1_r = check_input(bt1_r, 30)

    print(f'You have {30-bt1_w} WHITE pills, {30-bt1_b} BLACK pills and {30-bt1_r} RED pills remaining')
    print('\n')
    bt2_w = input('How many WHITE pills would like to put in bottle two?: ')
    bt2_w = check_input(bt2_w, 30-bt1_w)

    bt2_b = input('How many BLACK pills would like to put in bottle two?: ')
    bt2_b = check_input(bt2_b, 30-bt1_b)

    bt2_r = input('How many RED pills would like to put in bottle two?: ')
    bt2_r = check_input(bt2_r, 30-bt1_r)

    while ((bt2_w == 0) & (bt2_b == 0) & (bt2_r == 0)) or ((bt1_b == 30-bt1_w) & (bt2_b == 30-bt2_b) & (bt1_r == 30 - bt2_r) or ((30 - bt1_w - bt2_w) + (30 - bt1_b - bt2_b) + (30 - bt1_r - bt2_r)) < 1):
        print("Each bottle must contain at least one pill, please select again")
        bt2_w = input("How many WHITE pills would you like to put in bottle two?: ")
        bt2_w = check_input(bt1_w, 30-bt1_w)
        
        bt2_b = input("How many BLACK pills would you like to put in bottle two?: ")
        bt2_b = check_input(bt1_b, 30-bt1_b)

        bt2_r = input("How many RED pills would you like to put in bottle two?: ")
        bt2_r = check_input(bt1_r, 30-bt1_r)

    bt3_w = 30 - bt1_w - bt2_w
    bt3_b = 30 - bt1_b - bt2_b
    bt3_r = 30 - bt1_r - bt2_r

    print('\n')
    print(f"Bottle 1 contains {bt1_w} WHITE pills, {bt1_b} BLACK pills and {bt1_r} RED pills")
    print(f"Bottle 2 contains {bt2_w} WHITE pills, {bt2_b} BLACK pills and {bt2_r} RED pills")
    print(f"Bottle 3 contains {bt3_w} WHITE pills, {bt3_b} BLACK pills and {bt3_r} RED pills")
    print('\n')

    confirm = input('Are you happy with this selection? (yes/no): ')
    while (confirm != 'yes') and (confirm != 'no'):
        confirm = input('Are you happy with this selection? (yes/no): ')

        if confirm == 'no':
            crazy_warden_three()

    probability_one_two_ww = (bt1_w / (bt1_w + bt1_r + bt1_b)) * (bt2_w / (bt2_w + bt2_r + bt2_b))
    probability_one_two_rb = (bt1_r / (bt1_w + bt1_r + bt1_b)) * (bt2_b / (bt2_w + bt2_r + bt2_b))
    probability_one_two_br = (bt1_b / (bt1_w + bt1_r + bt1_b)) * (bt2_r / (bt2_w + bt2_r + bt2_b))
    
    probability_one_two = probability_one_two_ww + probability_one_two_rb +  probability_one_two_br

    probability_one_three_ww = (bt1_w / (bt1_w + bt1_r + bt1_b)) * (bt3_w / (bt3_w + bt3_r + bt3_b))
    probability_one_three_rb = (bt1_r / (bt1_w + bt1_r + bt1_b)) * (bt3_b / (bt3_w + bt3_r + bt3_b))
    probability_one_three_br = (bt1_b / (bt1_w + bt1_r + bt1_b)) * (bt3_r / (bt3_w + bt3_r + bt3_b))
    
    probability_one_three = probability_one_three_ww + probability_one_three_rb + probability_one_three_br

    probability_two_three_ww = (bt2_w / (bt2_w + bt2_r + bt2_b)) * (bt3_w / (bt3_w + bt3_r + bt3_b))
    probability_two_three_rb = (bt2_r / (bt2_w + bt2_r + bt2_b)) * (bt3_b / (bt3_w + bt3_r + bt3_b))
    probability_two_three_br = (bt2_b / (bt2_w + bt2_r + bt2_b)) * (bt3_r / (bt3_w + bt3_r + bt3_b))
    
    probability_two_three = probability_two_three_ww + probability_two_three_rb + probability_two_three_br

    probability = round(((1/3) * probability_one_two) + ((1/3) * probability_one_three) + ((1/3) * probability_two_three), 3)

    print('\n')
    print(f'If you were to select two bottles and a random pill from each, your probability of survival would be {probability}')
    print('\n')

    if probability == 0.553:
        print('This is your best chance of survival!')
        print('\n')
        print('Congratulations, you passed all three tests!')
        again_input = input('Would you like to try again? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to try again? (yes/no): ')
        
        if again_input == 'yes':
            from the_crazy_warden import crazy_warden_one_desc
        else:
            quit()

    elif probability < 0.553:
        again_input = input('This is not your best chance of survival, would you like try again? (yes/no): ')
        while (again_input != 'yes') and (again_input != 'no'):
            again_input = input('Would you like to try again? (yes/no): ')
        if again_input == 'yes':
            crazy_warden_three()
        else:
            quit()

crazy_warden_three_desc()