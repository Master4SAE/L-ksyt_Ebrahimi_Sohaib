import math

leivika = float(input("anna mitta leivisköinä"))
naula = float(input("anna mitta naulana"))
luoti = float(input("anna mitta luotina"))
ans1 = (leivika*20)*32*13.3
ans2 = (naula*32)*13.3
ans3 = luoti*13.3
ans4 = ans2+ans3+ans1
ans5 = math.floor(ans4/1000)
ans6 = ans4 - ans5
print(f'{ans5} kilo ja {ans6} gramma')
