print("Write a program that asks the user to enter numbers until they enter an empty string to quit. "
      "Finally, the program prints out the smallest and largest number from the numbers it received.")

largest = None
smallest = None

while True:
        num = input("Enter a number: ")
        if num == '':
            break
        n = int(num)
        largest = num
        if largest < num or largest == None:
            print("a")
        smallest = num
        if smallest > num or smallest == None:
            print("b")

print ("Maximum number is ", largest)
print ("Minimum number is ", smallest)









