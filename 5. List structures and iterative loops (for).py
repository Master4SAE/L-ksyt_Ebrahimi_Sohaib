#5.1
import random
print("Write a program that asks the user how many dice to roll. "
      "The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.")

users_input = int(input("how many times to roll the dice\n> "))

my_rolled_dices = []

rolling_dice = range(users_input)

for every_time in rolling_dice:
      dice = random.randint(1,6)
      print(dice)
      my_rolled_dices.append(dice)
print(f"the sum of all dices are {sum(my_rolled_dices)}")
