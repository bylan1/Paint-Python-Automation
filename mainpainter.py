import pyautogui
import keyboard
import random

# size of 1900 x 860 MS Paint canvas (minus 5)
xmin = 10
xmax = 1894
ymin = 149
ymax = 993

# drags a circle of radius 5 around cursor point
def circle_draw():
    pyautogui.move(0, -10)
    limitx = 5

    x = limitx
    y = 0

    while not (x == -limitx and y == 0):
        pyautogui.drag(x, y, 0, button="left")
        x -= 1
        if x >= 0:
            y += 1
        else:
            y -= 1

    while not (x == limitx and y == 0):
        pyautogui.drag(x, y, 0, button="left")
        x += 1
        if x <= 0:
            y -= 1
        else:
            y += 1

# random x y coords for cursor within canvas space and return location
def random_cursor():
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)
    pyautogui.moveTo(x, y, duration=0)
    return [x, y]

# output cursors current position
def cursor_position():
    x, y = pyautogui.position()
    print(f"Current Cursor Position - X: {x}, Y: {y}")

# draws line connecting points in the drawing order
def connect_points():
    length = len(coords)
    for i in range(length):
        if i == 0:
            pyautogui.moveTo(coords[i][0], coords[i][1])
        else:
            pyautogui.dragTo(coords[i][0], coords[i][1], duration=1, button="left")

coords = []

while True:
    try:
        input = keyboard.read_key()
        if input.isnumeric():
            num = int(input)
            while num > 0:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1
        if input == "`":
            cursor_position()
        if input == "-":
            coords.sort()       # sorts based on x-coord and then y-coord
            connect_points()
    except:
        break