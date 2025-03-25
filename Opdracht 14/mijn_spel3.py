import pgzrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor("robot_idle", (WIDTH // 2, HEIGHT - 50))
enemy = Actor("enemy", (random.randint(50, WIDTH - 50), 0))
score = 0
game_over = False

music.play("background.wav")

def draw():
    screen.fill((0, 0, 139))
    player.draw()
    enemy.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH//2, HEIGHT//2), fontsize=80, color="red")

def update():
    global score, game_over
    if not game_over:
        if keyboard.left and player.x > 50:
            player.x -= 5
        if keyboard.right and player.x < WIDTH - 50:
            player.x += 5
        if keyboard.up and player.y > 50:
            player.y -= 5
        if keyboard.down and player.y < HEIGHT - 50:
            player.y += 5
        
        enemy.y += 4
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(50, WIDTH - 50)
            score += 1
        
        if player.colliderect(enemy):
            try:
                music.play("hit.wav")
            except Exception as e:
                print("Geluid kon niet worden afgespeeld:", e)
            game_over = True

pgzrun.go()