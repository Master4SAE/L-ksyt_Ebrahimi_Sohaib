#5.1
import random

count_of_dice = []
go_to_loop = 0
ask_user_for_input = int(input("How many times should we roll the dice ?\n> "))

while go_to_loop != ask_user_for_input:
    rolling_the_dice = random.randint(1, 6)
    print(rolling_the_dice)
    count_of_dice.append(rolling_the_dice)
    go_to_loop = go_to_loop + 1
    
print(f"this is the sum of all rolled dices {sum(count_of_dice)}")
