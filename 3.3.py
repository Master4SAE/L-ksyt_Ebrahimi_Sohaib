suku_puoli = input(" Hei oletko mies tai nainen ? ").lower()
hemoglobin_arvo = float(input(" Anna hemoglobiiniarvo (g/l). " ))

#nainen
if (suku_puoli == 'nainen' and 117 <= hemoglobin_arvo <= 175):
    print("normaali")
elif suku_puoli == 'nainen' and hemoglobin_arvo < 117:
    print("alhainen")
elif suku_puoli == 'nainen' and hemoglobin_arvo > 175:
    print("korkea")
#mies
elif (suku_puoli == 'mies' and 134 <= hemoglobin_arvo <= 195):
    print("normaali")
elif suku_puoli == 'mies' and hemoglobin_arvo < 134:
    print("alhainen")
elif suku_puoli == 'mies' and hemoglobin_arvo > 195:
    print("korkea")
else:
    print(" ohjelma ei toimi !! ")


