import pgzrun
from pgzero.actor import Actor

width = 800
height = 600


speler = Actor("apple.png", (400, 300)) 
vijand = Actor("enemy.png", (400, 0))

def draw():
    screen.clear()
    speler.draw()
    vijand.draw()

def update():
    if keyboard.left and speler.x > 0:
        speler.x -= 5
    if keyboard.right and speler.x < width:
        speler.x += 5
    if keyboard.up and speler.y > 0:
        speler.y -= 5
    if keyboard.down and speler.y < height:
        speler.y += 5
    
    global vijand
    vijand.y += 3

    if vijand.y > height:
        vijand.y = 0


pgzrun.go()
