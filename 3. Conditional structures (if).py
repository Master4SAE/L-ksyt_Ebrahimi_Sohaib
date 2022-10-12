#3.1

kuhan_length = float(input(' Hei anna kuhan pituuden senttimetreinä '))
How_much_cm_is_left = 37- kuhan_length
if kuhan_length >= 37:
    print(" Toimi !")
else:
    print(f"laske takaisin järveen {How_much_cm_is_left} "
          f"senttiä alimmasta sallitusta pyyntimitasta puuttuu !")
    
#3.2

testi = input( )
print(testi.lower())

hytti_luokka = (input("Hei mitä hyttiluokan haluat ! "
                     "Tarjolla on LUX, A, B, C ").upper())
lux = 'LUX'
a = 'A'
b = 'B'
c = 'C'

if hytti_luokka == lux:
    print(" LUX on parvekkeellinen hytti yläkannella. ")
elif hytti_luokka == a:
    print(" A on ikkunallinen hytti autokannen yläpuolella. ")
elif hytti_luokka == b:
    print(" B on ikkunaton hytti autokannen yläpuolella. ")
elif hytti_luokka == c:
    print(" C on ikkunaton hytti autokannen alapuolella. ")
else:
    print("  Virheellinen hyttiluokka")
