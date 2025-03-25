import csv

def lees_csv_bestand(bestandsnaam):
    gegevens = []
    with open(bestandsnaam, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';') 
        for row in reader:
            gegevens.append(row)
    return gegevens

def toon_alle_gegevens(gegevens):
    for student in gegevens:
        print(f"Nummer: {student['Nummer']}, Naam: {student['Naam']}, HTML: {student['HTML']}, Python: {student['Python']}, Netwerken: {student['Netwerken']}, Rekenen: {student['Rekenen']}, IOT: {student['IOT']}, Nederlands: {student['Nederlands']}")

def zoek_student(gegevens, naam):
    for student in gegevens:
        if student['Naam'].lower() == naam.lower():
            return student
    return None

def toon_student_gegevens(student):
    if student:
        print(f"\nNummer: {student['Nummer']}")
        print(f"Naam: {student['Naam']}")
        print(f"HTML: {student['HTML']}")
        print(f"Python: {student['Python']}")
        print(f"Netwerken: {student['Netwerken']}")
        print(f"Rekenen: {student['Rekenen']}")
        print(f"IOT: {student['IOT']}")
        print(f"Nederlands: {student['Nederlands']}\n")
    else:
        print("Student niet gevonden.")

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

def main():
    bestandsnaam = './opdracht 12/proefwerken.csv'
    gegevens = lees_csv_bestand(bestandsnaam)
    
    if not gegevens:
        print("Fout: Geen gegevens gevonden in het CSV-bestand.")
        return
    
    hoofdmenu(gegevens)

# Programma starten
if __name__ == "__main__":
    main()
