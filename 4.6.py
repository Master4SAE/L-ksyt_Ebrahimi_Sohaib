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