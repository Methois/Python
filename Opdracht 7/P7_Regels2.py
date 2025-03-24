from time import sleep
import keyboard

while True:
    print("Dit is mijn tweede loop in python")
    sleep(0.5)
    if keyboard.is_pressed('esc'):
     break
