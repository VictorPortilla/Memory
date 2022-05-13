"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path
car = path('car.gif')
tiles = ["A", "B", "C", "D", "E", "F", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6"] * 2
state = {'mark': None}
hide = [True] * 64
winCount = 32
contTaps = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def youWin():
    """Draw square with "You Win" written on it"""
    up()
    goto(-120, 125)
    down()
    color('black', 'green')
    begin_fill()
    for count in range(2):
        forward(240)
        left(90)
        forward(50)
        left(90)
    end_fill()
    goto(0, 125)
    color('white')
    write("You Win!", font=('Arial', 30, 'normal'), align="center")


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global contTaps
    contTaps = contTaps + 1
    spot = index(x, y)
    mark = state['mark']
    goto(0,210)
    write(contTaps, font=("Arial", 30, "normal"), align = "center")

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        global winCount
        winCount = winCount - 1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25, y+5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center")

    update()
    if (winCount > 0):
        ontimer(draw, 100)
    else:
        youWin()
    

#shuffle(tiles)
setup(420, 460, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

