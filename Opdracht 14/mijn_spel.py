import pgzrun
from pgzero.actor import Actor

width = 800
height = 600

# Zorg ervoor dat de afbeelding in de 'images' map staat
speler = Actor("apple.png", (400, 300))  # Dit verwijst naar 'images/apple.png'

def draw():
    screen.clear()
    speler.draw()

def update():
    if keyboard.left and speler.x > 0:
        speler.x -= 5
    if keyboard.right and speler.x < width:
        speler.x += 5
    if keyboard.up and speler.y > 0:
        speler.y -= 5
    if keyboard.down and speler.y < height:
        speler.y += 5

pgzrun.go()
