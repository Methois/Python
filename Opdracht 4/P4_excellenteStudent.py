'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: Check of persoon een excellente student is
'''

# Vraag de student naar zijn naam
naam = input("Wat is je naam: ")

# vraag de student naar zijn cijfers
cijfer1 = float(input("Wat is het cijfer dat je voor proefwerk 1 hebt gehaald? "))
cijfer2 = float(input("Wat is het cijfer dat je voor proefwerk 2 hebt gehaald? "))
cijfer3 = float(input("Wat is het cijfer dat je voor proefwerk 3 hebt gehaald? "))
cijfer4 = float(input("Wat is het cijfer dat je voor proefwerk 4 hebt gehaald? "))
cijfer5 = float(input("Wat is het cijfer dat je voor proefwerk 5 hebt gehaald? "))

# vraagt de student hoeveel dagen die aanwezig is geweest
aanwezig = int(input("Hoeveel dagen ben je aanwezig geweest: "))

# bereken het gemiddelde cijfer
gemiddelde = ( cijfer1 + cijfer2 + cijfer3 + cijfer4 + cijfer5 ) / 5

# bereken het aanwezigheidspercentage
aanwezigpercentage = 100 / 120 * aanwezig

# print alle uitkomsten
print("Het gemiddelde cijfer van", naam, "is", gemiddelde)
print("Het aanwezigheidspercentage is " + str(int(aanwezigpercentage)) + "%")

#Bekijk of de leerling een excellente student is
if gemiddelde > 7.4:
    if aanwezigpercentage > 79:
        print(naam, "Is een excellente student")
else:
    print(naam, "Is geen Excellente student")

