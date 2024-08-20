from turtle import Screen, Turtle
from spaceship import Spaceship
from invader import Invader
from stars import Stars
from bullet import Bullet
from time import sleep, time
from random import randint, choice

# ---------- Screen Settings ----------
screen = Screen()
screen.title("Breakout")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# ---------- Stars ----------
for n in range(100):
    x = randint(-300, 300)
    y = randint(-300, 300)
    Stars(x, y)


# ---------- Spaceship ----------
ship = Spaceship((0, -200))

# ---------- Player Bullets ----------
player_bullets = []
last_shot_time = 0
shot_cooldown = 0.5  # second
def shoot():
    global last_shot_time
    current_time = time()
    if current_time - last_shot_time >= shot_cooldown:
        new_bullet = Bullet(ship.position(), 'white')
        new_bullet.setheading(90)
        player_bullets.append(new_bullet)
        last_shot_time = current_time

# ---------- Invaders' Bullets ----------
invader_bullets = []
def invader_shoot():
    shooting_invader = choice(invaders)
    new_bullet = Bullet(shooting_invader.position(), 'red')
    new_bullet.setheading(270)
    invader_bullets.append(new_bullet)


# ---------- Controls ----------
screen.listen()
screen.onkeypress(ship.go_left, "Left")
screen.onkeypress(ship.go_right, "Right")
screen.onkeypress(shoot, 'space')

# ---------- Invaders ----------
invaders = []
rows = 4
cols = 6
x_start = -100
y_start = 250
invader_width = 40
invader_height = 40

for row in range(rows):
    for col in range(cols):
        x = x_start + (col * invader_width)
        y = y_start - (row * invader_height)
        invader = Invader(x, y)
        invaders.append(invader)

# ---------- Game Loop ----------
game_is_on = True
while game_is_on:
    sleep(0.02)

    for invader in invaders:
        invader.move()
        # invaders collision with wall
        if invader.xcor() <= -290 or invader.xcor() >= 290:
            invader.bounce_x()

    # Player's bullet
    for bullet in player_bullets:
        bullet.move()
        for invader in invaders:
            # Bullet collision with invader
            if bullet.distance(invader) < 15 and bullet.ycor() <= invader.ycor():
                invader.hideturtle()
                invaders.remove(invader)
                bullet.hideturtle()
                if bullet in player_bullets:
                    player_bullets.remove(bullet)
        # check if bullet leaves screen
        if bullet.ycor() > 300:
            bullet.hideturtle()
            player_bullets.remove(bullet)

    # randomly have invaders shoot
    if randint(1, 100) < 5:  # 5% chance to shoot per frame
        invader_shoot()

    # Invaders' bullets
    for bullet in invader_bullets:
        bullet.move()
        # check if bullet leaves screen
        if bullet.ycor() < -300:
            bullet.hideturtle()
            invader_bullets.remove(bullet)

        # Invader's bullet collision with player
        if ship.distance(bullet) < 15 and bullet.ycor() <= ship.ycor():
            # game over
            game_is_on = False
            game_msg = Turtle()
            game_msg.penup()
            game_msg.hideturtle()
            game_msg.color('white')
            game_msg.write("GAME OVER", move=False, align="center", font=('ThaleahFat', 50, 'normal'))

    if not invaders:
        # game over
        game_is_on = False
        game_msg = Turtle()
        game_msg.penup()
        game_msg.hideturtle()
        game_msg.color('white')
        game_msg.write("YOU WIN!", move=False, align="center", font=('ThaleahFat', 50, 'normal'))

    screen.update()

screen.exitonclick()
