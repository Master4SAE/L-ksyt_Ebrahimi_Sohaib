lux = 'LUX'
lux1 = 'lux'
a = 'A'
b = 'B'
c = 'C'

hytti_luokka = (input("Hei mitä hyttiluokan haluat ! "
                     "Tarjolla on LUX, A, B, C "))
if hytti_luokka != lux || lux1:
    print(" LUX on parvekkeellinen hytti yläkannella. ")
elif hytti_luokka == a:
    print(" A on ikkunallinen hytti autokannen yläpuolella. ")
elif hytti_luokka == b:
    print(" B on ikkunaton hytti autokannen yläpuolella. ")
elif hytti_luokka == c:
    print(" C on ikkunaton hytti autokannen alapuolella. ")
else:
    print("  Virheellinen hyttiluokka")