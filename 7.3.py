
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