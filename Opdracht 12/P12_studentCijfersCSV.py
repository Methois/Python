import csv

# Functie om een CSV-bestand te lezen en de gegevens op te slaan in een lijst
# Dit zorgt ervoor dat we de studenten en hun cijfers kunnen gebruiken
def lees_csv_bestand(bestandsnaam):
    gegevens = []
    with open(bestandsnaam, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';') 
        for row in reader:
            gegevens.append(row)
    return gegevens

# Functie om een nieuwe student toe te voegen
def insertStudent(bestandsnaam, gegevens):
    print("Nieuwe student toevoegen")
    nummer = input("Nummer: ")
    naam = input("Naam: ")
    html = input("HTML cijfer: ")
    python = input("Python cijfer: ")
    netwerken = input("Netwerken cijfer: ")
    rekenen = input("Rekenen cijfer: ")
    iot = input("IOT cijfer: ")
    nederlands = input("Nederlands cijfer: ")
    
    nieuwe_student = {
        'Nummer': nummer,
        'Naam': naam,
        'HTML': html,
        'Python': python,
        'Netwerken': netwerken,
        'Rekenen': rekenen,
        'IOT': iot,
        'Nederlands': nederlands
    }
    
    gegevens.append(nieuwe_student)
    schrijf_csv_bestand(bestandsnaam, gegevens)
    print("Student toegevoegd!")

# Functie om een student te bewerken
def bewerkStudent(bestandsnaam, gegevens):
    naam = input("Voer de naam in van de student die je wilt bewerken: ")
    for student in gegevens:
        if student['Naam'].lower() == naam.lower():
            print("Bewerk de cijfers van de student. Laat leeg om te houden.")
            for vak in ['HTML', 'Python', 'Netwerken', 'Rekenen', 'IOT', 'Nederlands']:
                nieuw_cijfer = input(f"Nieuw cijfer voor {vak} ({student[vak]}): ")
                if nieuw_cijfer:
                    student[vak] = nieuw_cijfer
            schrijf_csv_bestand(bestandsnaam, gegevens)
            print("Student bijgewerkt!")
            return
    print("Student niet gevonden.")

# Functie om het CSV-bestand opnieuw op te slaan
def schrijf_csv_bestand(bestandsnaam, gegevens):
    velden = ['Nummer', 'Naam', 'HTML', 'Python', 'Netwerken', 'Rekenen', 'IOT', 'Nederlands']
    with open(bestandsnaam, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=velden, delimiter=';')
        writer.writeheader()
        writer.writerows(gegevens)

# Functie om alle studentenresultaten te tonen
def toonAlleStudentResultaten(gegevens):
    for student in gegevens:
        print("-" * 30)
        for key, value in student.items():
            print(f"{key}: {value}")
        print("-" * 30)

# Hoofdmenu met alle opties
def hoofdmenu(bestandsnaam, gegevens):
    while True:
        print("\nHoofdmenu:")
        print("1. Voeg een nieuwe student toe")
        print("2. Bewerk een student")
        print("3. Toon alle studentresultaten")
        print("4. Stop het programma")
        
        keuze = input("Kies een optie (1/2/3/4): ")
        
        if keuze == '1':
            insertStudent(bestandsnaam, gegevens)
        elif keuze == '2':
            bewerkStudent(bestandsnaam, gegevens)
        elif keuze == '3':
            toonAlleStudentResultaten(gegevens)
        elif keuze == '4':
            print("Programma wordt gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# Programma starten
def main():
    bestandsnaam = 'proefwerken.csv'
    gegevens = lees_csv_bestand(bestandsnaam)
    
    if not gegevens:
        print("Fout: Geen gegevens gevonden in het CSV-bestand.")
        return
    
    hoofdmenu(bestandsnaam, gegevens)

if __name__ == "__main__":
    main()