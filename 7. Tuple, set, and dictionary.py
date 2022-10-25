# 7.1

seasons = ("spring", "summer", "autumn", "winter")
user_input = int(input("Hey user give me a number of a month\n> "))
if user_input == 12 or user_input == 1 or user_input == 2:
    print(f"the season is {seasons[3]}")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print(f"the season is {seasons[2]}")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print(f"the season is {seasons[1]}")
elif user_input == 9 or user_input == 10 or user_input == 11:
    print(f"the season is {seasons[0]}")
else:
      print("Error 404")

#7.2

my_set = set()
mu_list = []

user_input = input("please give me names \n For exiting press enter \n> ")

while user_input != "":

    if user_input in my_set:
        print("existing name")
    else:
        print("new name")

    my_set.add(user_input)
    mu_list.append(user_input)

    user_input = input("please give me names \n For exiting press enter \n> ")
for name in mu_list:
      print(name)

#7.3        
# stored data
ico_code_airport_name = {"EFHK": "Helisnki-Vantaa Airport"}
# asks what to do
print(" hey do you want to add new airport, get information of a existing airport or quite ? ")
print(" for add press 1 "
      "for get press 2 "
      "for quite press 3 ")
# takes in input value
pressed_number = input("give me the number")
# changes str value to int
int_converter = int(pressed_number)

# goes into while
while True:
    # saves value again
    int_converter = int(pressed_number)
    # if user input is 1
    if int_converter == 1:
        # takes in ICAO code
        new_ico_code = input("Give me ICAO code")
        # takes in airport name
        new_airport_name = input(" Give me new airport name")
        # saves given values to dictionary
        ico_code_airport_name.update({new_ico_code: new_airport_name})
        # asks again
        pressed_number = input("give me the number")

    elif int_converter == 2:
        # asks for ICAO code
        give_me_ico_code = input(" Give me the ICAO code")
        # prints the value if the key matches
        print(ico_code_airport_name.get(give_me_ico_code))

        pressed_number = input("give me the number")

    elif int_converter == 3:
        # stops the code
        print("lopetettu")
        break
    else:
        # If number is not between 1-3 asks again
        print("Wrong number. Please try again")
        pressed_number = input("give me the number")
