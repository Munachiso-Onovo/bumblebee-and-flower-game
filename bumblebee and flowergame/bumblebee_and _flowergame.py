import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 500

score = 0
gameover = False


bee = Actor("bee.png")
flower = Actor("flower.png")

bee.pos = 100,100
flower.pos = 200,200

def draw():
    screen.blit("background.png",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text(str(score),(10,10),fontsize = 40)

    if gameover:
        screen.fill("green")
        screen.draw.text("The time is up",(10,10),fontsize = 40,color = "red")

def time_up():
    global gameover
    gameover = True


def update():
    global score
    
    if keyboard.left:
        bee.x = bee.x - 2
    
    if keyboard.right:
        bee.x = bee.x + 2

    if keyboard.up:
        bee.y = bee.y - 2

    if keyboard.down:
        bee.y = bee.y + 2

    flower_collected = bee.colliderect(flower)

    if flower_collected:
        move_flower()
        score = score + 10
        print(score)


def move_flower():
    flower.x = random.randint(50,500)
    flower.y = random.randint(50,450)
    

clock.schedule(time_up,60)


pgzrun.go()