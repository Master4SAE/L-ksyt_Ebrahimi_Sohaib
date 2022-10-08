#Tehtävä 2.1
name = input("Hei anna nimesi ! ")
print("terve " + name)

#Tehtävä 2.2
import math
print("hei tässä ohjelmassa lasketaan ympyrän pinta-ala !")
sade = float(input("Anna säde"))
pinta_ala = (sade*sade) * math.pi
print(pinta_ala)

#Tehtävä 2.3
kanta = float(input("anna kanta"))
korkeus = float(input("anna korkeus"))
pinta_ala = kanta * korkeus
piiri = 2*kanta + 2*korkeus
print(f'pinta-ala on {pinta_ala} ja piiri on {piiri}')

#Tehtävä 2.4
a = float(input('anna ensimmäinen kokonaisluku '))
b = float(input('anna toinen kokonaisluku '))
c = float(input('anna  kolmas kokonaisluku '))

summa = a+b+c
tulo = a*b*c
keski = (a+b+c)/3

print(f'kokonaislukujen summa on {summa} niiden tulo on {tulo} ja keski-arvo on {keski} ')

#Tehtävä 2.5
import math

leivika = float(input("anna mitta leivisköinä"))
naula = float(input("anna mitta naulana"))
luoti = float(input("anna mitta luotina"))
ans1 = (leivika*20)*32*13.3
ans2 = (naula*32)*13.3
ans3 = luoti*13.3
grammas = ans2+ans3+ans1
k_g = int(grammas/1000)
left_overs = math.floor(grammas % 1000)

print(f'{k_g} kilo ja {left_overs} gramma')

#Tehtävä 2.6
import random
print('Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia: '
      'kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.'
      'nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.')
value = random.randint(0 , 9)
value1 = random.randint(0,9)
value2 = random.randint(0,9)
print(value, value1, value2)

num = random.randint(1 , 6)
num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
print(num, num1, num2, num3)

