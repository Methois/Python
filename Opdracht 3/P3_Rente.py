'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: rente berekenen
'''

# Vraag de gebruiker om het bedrag en het rentepercentage
bedrag = float(input("Geef het bedrag: "))
rentepercentage = float(input("Geef het rentepercentage (bijv. 2.5): "))

# Bereken de te betalen rente
rente = bedrag * (rentepercentage / 100)
termijnbedrag = ( bedrag + rente )  / 12
afgerond = round(termijnbedrag, 2)
# Print de uitkomsten
print("Te betalen rente: " + str(rente))
print("Maandelijkse termijn over 12 maanden: " + str(afgerond))
