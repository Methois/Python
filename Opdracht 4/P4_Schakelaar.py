'''
auteur: Mathijs Berkelaar
datum: 23/09/2024
doel: Lamp schakelaar in python
'''

# de begin status van het lampje. ( In dit geval is dat "uit" )
lampje_status = "uit"

# De while loop zorgt er voor dat dit continue blijft herhalen. in dit geval blijft de input herhalen
while True:
    keuze = input("Wil je het lampje aan of uit zetten: ")

# checkt of de keuze die is gemaakt gelijk is aan 'aan'
    if keuze == 'aan':
        # controleert of het lampje al aan is op het moment
        if lampje_status == 'aan':
            print("Het lampje is al aan!")
        # mocht de status van het lampje niet aan zijn en er word aan getypt bij de input veranderd hij de status naar aan en print ie dat in de consolke
        else:
            lampje_status = 'aan'
            print("Lampje is aangezet")

    # checkt of de keuze die is gemaakt gelijk is aan 'uit'
    elif keuze == 'uit':
        if lampje_status == 'uit':
            print("Lampje is al uit")
        else:
            lampje_status = "uit"
            print("Lampje is uit gezet")

    # geeft een berichtje als zowel aan als uit niet is opgegeven bij de input
    else:
        print("Ongeldige invoer, Probeer het opnieuw")
