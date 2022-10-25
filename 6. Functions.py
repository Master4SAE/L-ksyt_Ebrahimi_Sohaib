#6.1
import random

def get_dice():
    my_dice = random.randint(1, 6)
    return my_dice


count = 1

while True:
    dice_rolled = get_dice()
    print(f"Its the {count} round and the dice rolled number is {dice_rolled}")
    count = count + 1
    if dice_rolled == 6:
        break
      
#6.2
import random


def get_dice():
    my_dice = random.randint(1, sides)
    return my_dice


sides = int(input("Hey how many sides should the dice have?\n > "))
count = 1

while True:
    dice_rolled = get_dice()
    print(f"Its the {count} round and the dice rolled number is {dice_rolled}")
    count = count + 1
    if dice_rolled == sides:
        break

#6.3

def get_converter(user_input):
    # 1 liter =0.264172052 US gallons
    convert = user_input * 3.785
    return convert


while True:
    user_input = float(input("Give me the volume in gallons!\n if negative value given program will end\n> "))
    if user_input < 0:
        break
    print(f"{user_input} Gallons is {get_converter(user_input)} liters")
