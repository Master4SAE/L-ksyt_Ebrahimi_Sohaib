print(f"Write a program that asks the user to enter numbers until they enter an empty string to quit.\n"
      f"Finally, the program prints out the smallest and largest number from the numbers it received.")

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






