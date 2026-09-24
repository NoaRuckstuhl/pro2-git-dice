from random import randint
from statistic import summe_berechnen, durchschnitt_berechnen

count = int(input("Wie oft sollen wir würfeln? "))

wuerfel_ergebnisse = []
for _ in range(count):
    ergebnis = randint(1,6)
    wuerfel_ergebnisse.append(ergebnis)


print("Summe:", summe_berechnen(wuerfel_ergebnisse))
print("Durchschnitte:", durchschnitt_berechnen(wuerfel_ergebnisse))