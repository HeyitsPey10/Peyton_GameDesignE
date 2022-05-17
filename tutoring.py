import turtle
import os
import random
import time

button1 = turtle.Turtle()
button2 = turtle.Turtle()
button3 = turtle.Turtle()
star_speed = 10

def setup_window(width, height):
    wn = turtle.Screen()
    wn.setup(width, height)
    wn.bgcolor("white")
    

def game_loop(x, y): #add in your game loop
    print(x, y)
    wn = turtle.Screen()
    wn = turtle.Screen()
    wn.title("Falling Down by @TokyoEdTech")
    wn.bgpic("images\\useClouds.gif")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    wn.register_shape("images\\transpBasket.gif")
    wn.register_shape("images\star1.gif")
    wn.register_shape("images\Star.gif")

        # Score
    score = 0

    # Health
    lives = 3

    # Player
    player = turtle.Turtle()
    player.speed(0)
    player.shape("images\\transpBasket.gif")
    # player.color("white")
    player.penup()
    player.goto(0, -250)
    player.direction = "stop"
    
    # Good things
    good_things = []

    for _ in range(3):
        good_thing = turtle.Turtle()
        good_thing.speed(10) #how fast the stars are falling
        good_thing.shape("images\Star.gif")
        # good_thing.color("green")
        good_thing.penup()
        good_thing.goto(-100, 250)
        #good_thing.speed = 1
        good_things.append(good_thing)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))

    # Functions
    def go_left():
        player.direction = "left"
        player.shape("images\\transpBasket.gif")
    
    def go_right():
        player.direction = "right"
        player.shape("images\\transpBasket.gif")

    def stop():
        player.direction = "none"

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")
    wn.onkeyrelease(stop, "Left")
    wn.onkeyrelease(stop, "Right")
    wn.update()

    
    while True:
        time.sleep(1.0/60)
        wn.update()
        
        # Move the player
        if player.direction == "left":
            player.setx(player.xcor() - 10)
        
        if player.direction == "right":
            player.setx(player.xcor() + 10)

        # Check for border collisions
        if player.xcor() < -390:
            player.setx(-390)
            
        elif player.xcor() > 390:
            player.setx(390)
            
        for good_thing in good_things:
            # Move the good things
            good_thing.sety(good_thing.ycor() - 10)

        # Check if good things are off the screen
            if good_thing.ycor() < -300:
                good_thing.goto(random.randint(-300, 300), random.randint(400, 800))

            # Check for collisions
            if player.distance(good_thing) < 40:
                # Score increases
                score += 10
            
                # Show the score
                pen.clear()
                pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            
                # Move the good thing back to the top
                good_thing.goto(random.randint(-300, 300), random.randint(400, 800))
         
         # Check for game over
        lives = 3
        score = 0
        if lives == 0:
            pen.clear()
            pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            wn.update()
            time.sleep(5)
            # score = 0
            # lives = 3
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
                





def add_button_1():
    button1.penup()
    button1.hideturtle()
    button1.shape("square")
    button1.goto(0, 260)
    button1.write("Instructions", align="center", font=("Courier", 24, "normal"))
    button1.onclick(lambda x, y: button1.clear(), 1, True)
    button1.onclick(lambda x, y: button1.hideturtle(), 1, True)
    button1.onclick(instructions)
    button1.showturtle()

def add_button_2():
    button2.penup()
    button2.hideturtle()
    button2.shape("square")
    button2.goto(0, 160)
    button2.write("Level 1", align="center", font=("Courier", 24, "normal"))
    button2.onclick(game_loop, 1, True)
    button2.onclick(lambda x, y: button1.clear(), 1, True)
    button2.onclick(lambda x, y: button1.hideturtle(), 1, True)
    # star_speed = 20
    # button2.onclick(instructions)
    button2.showturtle()

# def add_button3():
#     button3.penup()
#     button3.hideturtle()
#     button3.shape("square")
#     button3.goto(0, 140)
#     button3.write("Level 2", align="center", font=("Courier", 24, "normal"))
#     button3.onclick(game_loop2, 1, True)
#     button3.onclick(lambda x, y: button2.clear(), 1, True)
#     button3.onclick(lambda x, y: button2.hideturtle(), 1, True)
#     button3.showturtle()


def instructions(x, y):
    button1.hideturtle()
    button2.hideturtle()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.write("Use the arrow keys to move the basket and catch the stars.", align="center", font=("Courier", 16, "normal"))

setup_window(800, 600)
add_button_1()
add_button_2()
turtle.done()