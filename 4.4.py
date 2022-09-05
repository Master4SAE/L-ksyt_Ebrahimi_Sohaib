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






