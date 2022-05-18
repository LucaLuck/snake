import random
import math
import pgzrun


# Global constants
WIDTH = 600
HEIGHT = 400

BLUE = 24, 123, 205
BLACK = 0, 0, 0
GREEN = 77, 104, 33
BACKGROUND_COLOR = 119, 198, 110

UNIT_SIZE = 10

BORDER_TOP = Rect((0, 0), (WIDTH, UNIT_SIZE))
BORDER_LEFT = Rect((0, 0), (UNIT_SIZE, HEIGHT))
BORDER_BOTTOM = Rect((0, HEIGHT - UNIT_SIZE), (WIDTH, UNIT_SIZE))
BORDER_RIGHT = Rect((590, 0), (10, 400))


# Global variables
x = math.floor(random.randint(WIDTH / 5, 4 * WIDTH / 5) / UNIT_SIZE) * UNIT_SIZE
y = math.floor(random.randint(HEIGHT / 5, 4 * HEIGHT / 5) / UNIT_SIZE) * UNIT_SIZE


def draw():
    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw borders
    screen.draw.filled_rect(BORDER_TOP, GREEN)
    screen.draw.filled_rect(BORDER_LEFT, GREEN)
    screen.draw.filled_rect(BORDER_BOTTOM, GREEN) 
    screen.draw.filled_rect(BORDER_RIGHT, GREEN)

    # Draw snake (1 square for now)
    patrat = Rect((x, y), (UNIT_SIZE, UNIT_SIZE))
    screen.draw.filled_rect(patrat, BLUE)
    screen.draw.rect(patrat, BLACK)


def update() :
    global y
    global x

    if  keyboard.up :
        y = y - UNIT_SIZE
    elif keyboard.down :
        y = y + UNIT_SIZE
    elif keyboard.left:
        x = x - UNIT_SIZE
    elif keyboard.right :
        x = x + UNIT_SIZE  


pgzrun.go()
