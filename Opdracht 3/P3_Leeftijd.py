'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: leeftijd berekenen
'''
import datetime
huidigjaar = datetime.datetime.year

# Vraag de gebruiker om de naam & geboortejaar
naam = input("Geef je naam: ")
geboortejaar = int(input("Geef je geboortejaar: "))  # Zet de invoer om naar een integer

# de som voor leeftijd
leeftijd = huidigjaar - geboortejaar

# Print de naam & leeftijd
print("Hallo " + naam)
print("Je bent " + str(leeftijd) + " jaar oud")
