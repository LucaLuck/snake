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
def random_food(avoidList):

    while True:
        x_food = math.floor(random.randint(UNIT_SIZE, WIDTH - 2 * UNIT_SIZE) / UNIT_SIZE) * UNIT_SIZE
        y_food = math.floor(random.randint(3 * UNIT_SIZE, HEIGHT - 2 * UNIT_SIZE) / UNIT_SIZE) * UNIT_SIZE

        #if (x_avoid == 0 and y_avoid == 0) or (x_avoid != x_food or y_avoid != y_food) :
        if not ((x_food, y_food) in snake) :
            return (x_food, y_food)


# Global variables
snake = [(math.floor(random.randint(WIDTH / 5, 4 * WIDTH / 5) / UNIT_SIZE) * UNIT_SIZE, math.floor(random.randint(HEIGHT / 5, 4 * HEIGHT / 5) / UNIT_SIZE) * UNIT_SIZE)]

xFood, yFood = random_food(snake)
print("Food at: ", xFood, yFood)

score = 0
xSpeed = 0 
ySpeed = 0
gameSpeed = 0.3
gameOver = False;


def updateStateOnClock():
    global snake
    global xFood, yFood, score
    global gameOver

    if gameOver :
        return

    x_head = snake[0][0]
    y_head = snake[0][1]

    x_newHead = x_head + xSpeed * UNIT_SIZE
    y_newHead = y_head + ySpeed * UNIT_SIZE

    snake.insert(0, (x_newHead, y_newHead))

    if x_newHead == xFood and y_newHead == yFood : 
        score = score + 1
        xFood, yFood = random_food(snake)
        print("New food at: ", xFood, yFood)
    else :
        snake.pop()

    # check if the new head is out of bounds. In this case stop the game.
    if y_newHead <= UNIT_SIZE + 20 or \
        y_newHead >= HEIGHT - 2 * UNIT_SIZE or \
        x_newHead <= UNIT_SIZE or \
        x_newHead >= WIDTH - 2 * UNIT_SIZE :
        gameOver = True; # TODO: display game over or something and allow re-play

    return

clock.schedule_interval(updateStateOnClock, gameSpeed)

def draw():
    global snake
    
    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw borders
    screen.draw.filled_rect(BORDER_TOP, GREEN)
    screen.draw.filled_rect(BORDER_LEFT, GREEN)
    screen.draw.filled_rect(BORDER_BOTTOM, GREEN) 
    screen.draw.filled_rect(BORDER_RIGHT, GREEN)

    # Draw snake
    for s in snake :
        r = Rect((s[0], s[1]), (UNIT_SIZE, UNIT_SIZE))
        screen.draw.filled_rect(r, BLUE)
        screen.draw.rect(r, BLACK)

    #draw food
    food = Rect((xFood, yFood), (UNIT_SIZE, UNIT_SIZE))
    screen.draw.filled_rect(food, RED)
    
    #draw score
    screen.draw.text("Score: " + str(score), (0, UNIT_SIZE))


def update() :
    global xFood
    global yFood
    global score
    global xSpeed
    global ySpeed

    if keyboard.up :
        xSpeed = 0
        ySpeed = -1
    elif keyboard.down :
        xSpeed = 0
        ySpeed = 1
    elif keyboard.left:
        xSpeed = -1
        ySpeed = 0
    elif keyboard.right :
        xSpeed = 1
        ySpeed = 0

pgzrun.go()



# de morgan law
# p = True
# q = False

# (p and q) == not (p or q)
# (p or q) == not (p and q)

