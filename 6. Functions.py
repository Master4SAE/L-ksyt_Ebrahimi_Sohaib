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

