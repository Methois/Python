'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: Premie van een autoverzekering berekenen
'''
# variable om de korting bij te houden
korting = 0

# vraagt de leeftijd & aantal schadevrijen jaren
leeftijd = input("Hoe oud bent u: ")
schadevrij = int(input("Hoeveel jaar heeft u gereden zonder schade: "))

# Voeg korting toe op basis van schadevrije jaren
if schadevrij > 9:
    korting += 10
elif schadevrij > 4:
    korting += 5

# Voeg extra korting toe voor leeftijd boven 25
if int(leeftijd) > 24:
    korting += 5

# berekend de korting op de bedragen en laat de bedragen zien zodat de klant een keuze kan maken
procent = 100 - korting

basis = 40 / 100 * procent
meer = 50 / 100 * procent
volledig = 60 / 100 * procent

print("Maak nu de keuze voor welke verzekering je neemt,\n1. Basis verzekerd -", basis, "€\n2. Meer verzekerd -", meer, "€\n3. Volledig verzekerd -", volledig, "€\n")
keuze = input("Welke verzekering wilt u nemen, Kies tussen 1, 2 of 3: ")

# op basis van de keuze krijg je te weten hoeveel je moet betalen
match keuze:
    case "1":
        print("Je hebt gekozen voor de basis( WA ) verzekering Gekozen. Je moet maandelijks", basis, "Betalen!")
    case "2":
        print("Je hebt gekozen voor de meer ( Wa + beperkt casco ) verzekering. Je moet maandelijks", meer, "Betalen!")
    case "3":
        print("Je hebt gekozen voor de volledig ( Wa + volledig casco ) verzekering. Je moet maandelijks", volledig, "Betalen!")
    case _:
        print("Ongeldige verzekeringstype gekozen.")







