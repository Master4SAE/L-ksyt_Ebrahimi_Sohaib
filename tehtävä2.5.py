import math

leivika = float(input("anna mitta leivisköinä"))
naula = float(input("anna mitta naulana"))
luoti = float(input("anna mitta luotina"))
ans1 = (leivika*20)*32*13.3
ans2 = (naula*32)*13.3
ans3 = luoti*13.3
grammas = ans2+ans3+ans1
k_g = int(grammas/1000)
left_overs =grammas % 1000

print(f'{k_g} kilo ja {left_overs} gramma')
