value_in_inches = float(input("Hello customer give me the value in inches! "))
convert_to_cm = value_in_inches * 2.51
while convert_to_cm >= 0:
    print(convert_to_cm)
    break
else:
    print(" The END")
