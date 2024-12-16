import turtle
import time
import random
import os

WIDTH = 500
HEIGHT = 500

COLORS = ['blue','red','pink','yellow','purple','orange','green','black']
def get_number_racers():

    while True:
        racers = input('Enter number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('PLEASE enter a digit ....')
            continue

        if 2 <= racers <=10:
            return racers
        else:
            print('Enter a racers into the 2-10 ...')

def race(colors):
    turtles = create_turtles(colors,racers)
    
    while True:
        for racer in turtles:
            distance = random.randint(1,5)
            racer.forward(distance)

            x, y = racer.pos()

            if y >= HEIGHT//2 - 30:
                return colors[turtles.index(racer)]

def create_turtles(colors,racers):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)

    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        if racers<=4:
            racer.shapesize(2,2)
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('TURTLE RACING')


racers = get_number_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]

init_turtle()
winner = race(colors)

print('the WINNER IS ',winner)

time.sleep(2)
os.system('clear')


