print("Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi."
      " Vuosi on karkausvuosi, jos se on jaollinen neljällä. "
      "Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.")

vuosi_luku = int(input("Hei anna vuosiluku"))

if vuosi_luku % 4 == 0:
    print("vuosi on karkausvuosi")
elif vuosi_luku % 4 != 0:
    print("ei ole karkausvuosi")
elif vuosi_luku % 100 == 0 and vuosi_luku % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkaus vuosi")