'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: Rekenmachine
'''

# Vraag om de getallen & Operator
getal1 = int(input("Voer het eerste getal in: "))
operator = input("Voeg een operator toe (+, -, *, /): ")
getal2 = int(input("Voer het tweede getal in: "))

# checkt of de operator + is, Zo ja berekend ie de uitkomst en print het, zo nee gaat ie door
if operator == "+":
    uitkomst = getal1 + getal2
    print("De getallen zijn bij elkaar opgeteld")
    print("Het antwoord is: " + str(uitkomst))

# checkt of de operator - is, Zo ja berekend ie de uitkomst en print het, zo nee gaat ie door
elif operator == "-":
    uitkomst = getal1 - getal2
    print("De getallen zijn van elkaar afgetrokken")
    print("Het antwoord is: " + str(uitkomst))

# checkt of de operator * is, Zo ja berekend ie de uitkomst en print het, zo nee gaat ie door
elif operator == "*":
    uitkomst = getal1 * getal2
    print("De getallen zijn vermenigvuldigd")
    print("Het antwoord is: " + str(uitkomst))

# checkt of de operator / is, Zo ja berekend ie de uitkomst en print het, zo nee gaat ie door
elif operator == "/":
    if getal2 != 0:  # Controleer of je niet door nul deelt
        uitkomst = getal1 / getal2
        print("De getallen zijn gedeeld")
        print("Het antwoord is: " + str(uitkomst))
    else:
        print("Fout: Delen door nul is niet toegestaan.")
# Als het geen van de operators zijn geeft ie een berichtje dat ze geen goeie operator hebben ingevuld
else:
    print("Ongeldige operator. Gebruik +, -, *, of /.")
