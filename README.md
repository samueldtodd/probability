# Probability
Probability puzzles and challenges simulated using Python. All code can be run in the terminal.

## [Dice Roll](dice_roll.py)

You're offered the following bet: two dice will be rolled simultaneously, if neither die show a 5 or 6 you win. If either die shows 5 or 6, you lose. Should you take the bet? This Python script uses object-orientated programming to produce a die class which includes a method to simulate the rolling of dice. The user is first asked whether they take the bet and then asked to enter the number of simulations they wish to run. The game is then run for the desired number of simulations and the proportion of games in which the user won is returned. Different messages are printed based on whether or not the user took the bet. The user then has the option to view an explanation how the probability of winning can be calculated. While loops and try/exception are utilised to ensure user input is appropriate.

## [Two Marbles Part One](two_marbles_part_one.py)

This problem is taken from the Perplexing Probability section found on brilliant.org. Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is placed into the bag. If the coin is tails, a blue marble is put into the bag. You can't observe the coin flip or the marbles. You pick out a marble at random from the bag. It's red. You place it back into the bag. What is the chance that you pull out a blue marble next time? This Python script simulates this scenario a number of times as input by the user. First the problem is presented, the desired number of simulations is input, and then using for loops and the random module the scenario is simulated. The percentage of scenarios in which a blue marble is pulled out is calculated and printed for the user. A function comprised of a while loop and try/exception is used to ensure user-input is an integer greater than zero.

## [Two Marbles Part Two](two_marbles_part_two.py)

A follow up to the above Two Marbles problem. Two marbles are placed into a bag determined by a coin flip. If the coin is heads, a red marble is put into the bag. If the coin is tails, a blue marble is put into the bag. You look into the bag and see at least one of the marbles is red. A red marble is set aside. What are the odds the remaining marble is blue? Using for loops and the random module, this Python script simulates this scenario a number of times as input by the user and returns the final probability.
