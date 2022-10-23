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

#5.3
print("Write a program that asks the user for an integer and tells if the number is a prime number."
      " Prime numbers are number that are only divisible by one or the number itself."
      "For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer."
      "On the other hand, 21 is not a prime number as it is divisible by 3 and 7.")

user_input = int(input("Hey user give me a integer\n> "))

if user_input > 1:
    print("we in prime check")

    for num in range(2, user_input):
        if (user_input % num) == 0:
            print(user_input, "is not a prime number")
            print(num, "times", user_input // num, "is", user_input)
            break
    else:
        print(user_input, "is a prime number")
else:
    print("The number you gave was not prime")

#5.4
#print("Write a program that asks the user to enter the names of five cities one by on "
#      "(use a for loop for reading the names) and stores them into a list structure."
#      " Finally, the program prints out the names of the cities one by one,"
#      " one city per line, in the same order they were read as input."
#      " Use a for loop for asking the names and a for/in loop to iterate through the list.")
city_names = []

for i in range(0, 5):
    print("enter the names of five cities one by one")
    user_input = input("City ? > ")
    city_names.append(user_input)

for city in city_names:
    print(city)
