# Begin met het instellen van de kosten op 0
kosten = 0

# Print het koffiemenu
print("Koffie menu\n")
print("Zwart")
print("1. Espresso.............2,50")
print("2. Americano............3,25\n")
print("Wit")
print("3. Cappuccino...........3,00")
print("4. Latte................3,20")
print("5. Flat white...........3,50\n")
print("Extra suiker...........0,25")

# Vraag om een keuze uit het menu
keuze = int(input("Maak uw keuze: "))
# Vraag of er extra suiker gewenst is, en zet het antwoord om naar kleine letters
suiker = input("Had u ook extra suiker gewild? (Ja/nee): ").lower()

# Maak een lijst met de koffiekeuzes en prijzen
menu = {
    1: (2.50, "Espresso"),
    2: (3.25, "Americano"),
    3: (3.00, "Cappuccino"),
    4: (3.20, "Latte"),
    5: (3.50, "Flat white")
}

# Functie die kijkt of de keuze geldig is en de prijs toevoegt aan de kosten
def kies_koffie():
    global kosten  # Zorg ervoor dat we de globale variabele kosten aanpassen
    if keuze in menu:  # Controleer of de keuze in het menu staat
        kosten += menu[keuze][0]  # Voeg de prijs van de gekozen koffie toe aan kosten
        print(f"Je hebt gekozen voor {menu[keuze][1]}")
        voeg_suiker_toe()  # Ga door naar de suikeroptie
    else:
        print("Keuze bestaat niet, begin opnieuw")
        kies_koffie()  # Start het programma opnieuw als de keuze ongeldig is

# Functie die kijkt of er suiker moet worden toegevoegd en de prijs bijwerkt
def voeg_suiker_toe():
    global kosten
    if suiker == "ja":
        kosten += 0.25  # Voeg €0,25 toe voor extra suiker
        print("Je hebt ook voor extra suiker gekozen")
    else:
        print("Je hebt niet voor extra suiker gekozen")

    print("Dit maakt het totaal:", kosten)  # Print het eindbedrag

kies_koffie()
