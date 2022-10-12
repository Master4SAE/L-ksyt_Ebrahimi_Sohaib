#4.1

num = 3
while num <= 1000:
    print(num)
    num = num +3
    
#4.2

value_in_inches = float(input("Hello customer give me the value in inches! "))
convert_to_cm = value_in_inches * 2.51

while convert_to_cm >= 0:
    print(convert_to_cm)
    value_in_inches = float(input("Hello customer give me the value in inches! "
                                  "If you want program to stop give it value lower than zero "))
    convert_to_cm = value_in_inches * 2.51

else:
    print(" THE END")
    
#4.3

smallest_number = largest_number = user_input = input(f" Hey give me numbers \n"
                       f"if you want to quit enter empty string ")

while user_input != "":

    user_input = input(f" Hey give me numbers \n"
                       f"if you want to quit enter empty string ")

    if user_input == '':
        break
    elif user_input != '':
        convert_to_int = int(user_input)

        if int(largest_number) < convert_to_int:
            largest_number = convert_to_int

        if int(smallest_number) > convert_to_int:
            smallest_number = convert_to_int

print(f" The largest number is {largest_number}")

print(f" The smallest number is {smallest_number}")

#4.4

import random
random_number = random.randint(1,10)
input_number = 0

while input_number != random_number:
    if input_number > random_number:
        print("liian suuri arvaus")
    elif input_number < random_number:
        print("liian pieni arvaus ")
    input_number = int(input(" anna arvaus 1-10 väliltä "))
    if input_number == random_number:
        print(" arvaus meni oikein !!! ")

#4.5

user_name = 'python'
pass_word = 'rules'

give_username = None
give_password = None

wrong = 2

give_username = input(" hey give me your username")
give_password = input(" hey give me your password")

if user_name != give_username or pass_word != give_password and pass_word != give_password:
    while 6 > wrong:
        give_username = input(" hey give me your username")
        give_password = input(" hey give me your password")

        if user_name == give_username and pass_word == give_password:
            print("Welcome.")
            break

        if wrong == 5:
            print("Access denied.")
            break

        wrong = wrong + 1

#4.6

import random
on_circle = 0

number_user_input = int(input("Anna  numero !"))

outer_of_numbers = 0

while outer_of_numbers <=number_user_input:
      y = random.uniform(-1, 1)
      x = random.uniform(-1, 1)
      if y ** 2 + x ** 2 <=1:
            on_circle += 1
      outer_of_numbers += 1

result = 4 * on_circle / number_user_input

print(result)
