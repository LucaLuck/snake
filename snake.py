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
GRAY = 162, 209, 73
BACKGROUND_COLOR = 170, 215, 81

UNIT_SIZE = 20

BORDER_TOP = Rect((0, 0), (WIDTH, UNIT_SIZE * 2))
BORDER_LEFT = Rect((0, 0), (UNIT_SIZE, HEIGHT))
BORDER_BOTTOM = Rect((0, HEIGHT - UNIT_SIZE), (WIDTH, UNIT_SIZE))
BORDER_RIGHT = Rect((WIDTH - UNIT_SIZE, 0), (UNIT_SIZE, HEIGHT))

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

    xHead = snake[0][0]
    yHead = snake[0][1]

    xNewHead = xHead + xSpeed * UNIT_SIZE
    yNewHead = yHead + ySpeed * UNIT_SIZE

    snake.insert(0, (xNewHead, yNewHead))

    if xNewHead == xFood and yNewHead == yFood : 
        score = score + 1
        xFood, yFood = random_food(snake)
        print("New food at: ", xFood, yFood)
    else :
        snake.pop()

    # check if the new head is out of bounds. In this case stop the game.
    if yNewHead <= UNIT_SIZE + 20 or \
        yNewHead >= HEIGHT - 2 * UNIT_SIZE or \
        xNewHead <= UNIT_SIZE or \
        xNewHead >= WIDTH - 2 * UNIT_SIZE :
        gameOver = True; # TODO: display game over or something and allow re-play

    return

clock.schedule_interval(updateStateOnClock, gameSpeed)


def drawBackground():
    screen.fill(BACKGROUND_COLOR)

    # Draw borders
    screen.draw.filled_rect(BORDER_TOP, GREEN)
    screen.draw.filled_rect(BORDER_LEFT, GREEN)
    screen.draw.filled_rect(BORDER_BOTTOM, GREEN) 
    screen.draw.filled_rect(BORDER_RIGHT, GREEN)

    lines = HEIGHT // UNIT_SIZE - 3
    columns = WIDTH // UNIT_SIZE - 2

    for line in range(0, lines) :
        for col in range(0, columns, 2) :
            x = (col + 1 + line % 2) * UNIT_SIZE
            y = (line + 2) * UNIT_SIZE
            r = Rect((x, y), (UNIT_SIZE, UNIT_SIZE))
            screen.draw.filled_rect(r, GRAY)

    #for line in xrange() :


def draw():
    global snake
    
    # Fill background
    drawBackground()

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

    # TODO: do not allow to change direction from left <-> rigt and up <-> down (ignore these transitions)
    if keyboard.up and ySpeed != 1 :
        xSpeed = 0
        ySpeed = -1
    elif keyboard.down and ySpeed != -1:
        xSpeed = 0
        ySpeed = 1
    elif keyboard.left and xSpeed != 1:
        xSpeed = -1
        ySpeed = 0
    elif keyboard.right and xSpeed != -1:
        xSpeed = 1
        ySpeed = 0

pgzrun.go()



# de morgan law
# p = True
# q = False

# (p and q) == not (p or q)
# (p or q) == not (p and q)

