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

#5.2
print("2.Write a program that asks the user to enter numbers until they input an empty string to quit."
      " At the end, the program prints out the five greatest numbers sorted in descending order."
      " Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.")

number_list = []

user_input = input("Hey enter numbers !\n For quiting press Enter\n> ")

while user_input != "":
    number_list.append(int(user_input))
    user_input = input("Hey enter numbers !\n For quiting press Enter\n> ")

number_list.sort(reverse=True)

print(number_list[0:5])
