import pygame
from pgzero.actor import Actor

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
speler = Actor("alien.png", (400, 300))

def draw():
    screen.clear()
    speler.draw()

def update():
    if keyboard.left:
        speler.x -= 5
    if keyboard.right:
        speler.x += 5