import random
import math
import pgzrun


# Global constants
WIDTH = 600
HEIGHT = 400

RED = 255, 0, 0
BLUE = 24, 123, 205
BLACK = 0, 0, 0
GREEN = 77, 104, 33
BACKGROUND_COLOR = 119, 198, 110

UNIT_SIZE = 10

BORDER_TOP = Rect((0, 0), (WIDTH, UNIT_SIZE + 20))
BORDER_LEFT = Rect((0, 0), (UNIT_SIZE, HEIGHT))
BORDER_BOTTOM = Rect((0, HEIGHT - UNIT_SIZE), (WIDTH, UNIT_SIZE))
BORDER_RIGHT = Rect((590, 0), (10, 400))

# functions
def random_food(x_avoid = 0, y_avoid = 0):

    while True:
        x_food = math.floor(random.randint(UNIT_SIZE, WIDTH - 2 * UNIT_SIZE) / UNIT_SIZE) * UNIT_SIZE
        y_food = math.floor(random.randint(3 * UNIT_SIZE, HEIGHT - 2 * UNIT_SIZE) / UNIT_SIZE) * UNIT_SIZE

        if (x_avoid == 0 and y_avoid == 0) or (x_avoid != x_food or y_avoid != y_food) :
            return (x_food, y_food)


# Global variables
x_snake = math.floor(random.randint(WIDTH / 5, 4 * WIDTH / 5) / UNIT_SIZE) * UNIT_SIZE
y_snake = math.floor(random.randint(HEIGHT / 5, 4 * HEIGHT / 5) / UNIT_SIZE) * UNIT_SIZE

x_food, y_food = random_food()
print("Food at: ", x_food, y_food)

score = 0
x_speed = 0 
y_speed = 0


def updateStateOnClock():
    global x_snake
    global y_snake
    global x_food, y_food, score

    x_snake = x_snake + x_speed * UNIT_SIZE
    y_snake = y_snake + y_speed * UNIT_SIZE

    if y_snake <= UNIT_SIZE + 20 : # check this out! why 20 code review
        y_snake = UNIT_SIZE + 20

    if y_snake >= HEIGHT - 2 * UNIT_SIZE :
        y_snake = HEIGHT - 2 * UNIT_SIZE

    if x_snake <= UNIT_SIZE:
        x_snake = UNIT_SIZE

    if x_snake >= WIDTH - 2 * UNIT_SIZE :
        x_snake = WIDTH - 2 * UNIT_SIZE

    if x_snake == x_food and y_snake == y_food : 
        score = score + 1
        x_food, y_food = random_food(x_snake, y_snake)
        print("New food at: ", x_food, y_food)

    return

clock.schedule_interval(updateStateOnClock, 0.1)

def draw():
    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw borders
    screen.draw.filled_rect(BORDER_TOP, GREEN)
    screen.draw.filled_rect(BORDER_LEFT, GREEN)
    screen.draw.filled_rect(BORDER_BOTTOM, GREEN) 
    screen.draw.filled_rect(BORDER_RIGHT, GREEN)

    # Draw snake (1 square for now)
    snake = Rect((x_snake, y_snake), (UNIT_SIZE, UNIT_SIZE))
    screen.draw.filled_rect(snake, BLUE)
    screen.draw.rect(snake, BLACK)

    #draw food
    food = Rect((x_food, y_food), (UNIT_SIZE, UNIT_SIZE))
    screen.draw.filled_rect(food, RED)
    
    #draw score
    screen.draw.text("Score: " + str(score), (0, UNIT_SIZE))


def update() :
    global y_snake
    global x_snake
    global x_food
    global y_food
    global score
    global x_speed
    global y_speed

    if keyboard.up :
        x_speed = 0
        y_speed = -1
    elif keyboard.down :
        x_speed = 0
        y_speed = 1
    elif keyboard.left:
        x_speed = -1
        y_speed = 0
    elif keyboard.right :
        x_speed = 1
        y_speed = 0

pgzrun.go()



# de morgan law
# p = True
# q = False

# (p and q) == not (p or q)
# (p or q) == not (p and q)

