import csv

# Functie om het CSV-bestand in te lezen
def lees_csv_bestand(bestandsnaam):
    gegevens = []
    with open(bestandsnaam, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gegevens.append(row)
    return gegevens

# Functie om alle gegevens te tonen
def toon_alle_gegevens(gegevens):
    for student in gegevens:
        print(f"Naam: {student['Naam']}, Leeftijd: {student['Leeftijd']}, Klas: {student['Klas']}, Cijfer: {student['Cijfer']}")

# Functie om een specifieke student te zoeken
def zoek_student(gegevens, naam):
    for student in gegevens:
        if student['Naam'].lower() == naam.lower():
            return student
    return None

# Functie om de gegevens van een specifieke student te tonen
def toon_student_gegevens(student):
    if student:
        print(f"Naam: {student['Naam']}")
        print(f"Leeftijd: {student['Leeftijd']}")
        print(f"Klas: {student['Klas']}")
        print(f"Cijfer: {student['Cijfer']}")
    else:
        print("Student niet gevonden.")

# Functie voor het hoofdmenu
def hoofdmenu(gegevens):
    while True:
        print("\nHoofdmenu:")
        print("1. Toon alle gegevens")
        print("2. Zoek een specifieke student")
        print("3. Stop het programma")
        
        keuze = input("Kies een optie (1/2/3): ")
        
        if keuze == '1':
            toon_alle_gegevens(gegevens)
        elif keuze == '2':
            naam = input("Voer de naam van de student in: ")
            student = zoek_student(gegevens, naam)
            toon_student_gegevens(student)
        elif keuze == '3':
            print("Programma wordt gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# Hoofdprogramma
def main():
    bestandsnaam = 'proefwerken.csv'  # Zorg ervoor dat het bestand in de juiste directory staat
    gegevens = lees_csv_bestand(bestandsnaam)
    hoofdmenu(gegevens)

# Programma starten
if __name__ == "__main__":
    main()
