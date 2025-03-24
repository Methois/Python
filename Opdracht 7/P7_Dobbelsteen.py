from random import randint

while True:
    getal = randint(1, 6)
    print("Er is een getal getrokken tussen 1 en 6.")
    
    pogingen = 0 
    geraden = False 
    
    while pogingen < 3:
        guess = int(input("Raad eens welk getal het is: "))
        pogingen += 1  
        
        if guess < getal:
            print("Het getal is groter, raad nog eens.")
        elif guess > getal:
            print("Het getal is kleiner, raad nog eens.")
        else:
            print("Gewonnen! Het getal was", getal)
            geraden = True
            break 
    
    if not geraden:
        print("Helaas, je hebt het niet geraden. Het getal was", getal)
    
    opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Bedankt voor het spelen!")
        break 
