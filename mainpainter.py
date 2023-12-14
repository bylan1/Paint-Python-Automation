import pyautogui
import keyboard
import random
from scipy.spatial import ConvexHull
import sys

# size of 1900 x 860 MS Paint canvas (minus 5)
xmin = 10
xmax = 1894
ymin = 149
ymax = 993

coords = []

# drags a circle of radius 5 around cursor point
def circle_draw():
    pyautogui.move(0, -8)
    limitx = 6

    x = limitx
    y = 0

    while not (x == -limitx and y == 0):
        pyautogui.drag(x, y, 0, button="left")
        x -= 2
        if x >= 0:
            y += 2
        else:
            y -= 2

    while not (x == limitx and y == 0):
        pyautogui.drag(x, y, 0, button="left")
        x += 2
        if x <= 0:
            y -= 2
        else:
            y += 2

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

# convex hull solution
def compute_conv_hull(a):
    points = [(x,y) for x, y in a]
    ret = ConvexHull(points)
    return [points[vertex] for vertex in ret.vertices]

# draws line connecting points in the drawing order
def connect_points():
    if len(coords) > 2:
        edge_points = compute_conv_hull(coords)
        edge_points.append(edge_points[0])      # adds last point to loop convex hull
    else:
        edge_points = coords
    length = len(edge_points)

    for i in range(length):
        if i == 0:
            pyautogui.moveTo(edge_points[i][0], edge_points[i][1])
        else:
            pyautogui.dragTo(edge_points[i][0], edge_points[i][1], duration=1, button="left")

def test(e):
    if e.name == "esc":
        print("Successful termination")
        # terminate script

keyboard.hook(test)

while True:
    try:
        input = keyboard.read_key()
        if keyboard.is_pressed("ctrl+1"):
            coords.sort()       # sorts based on x-coord and then y-coord
            connect_points()
            break
        elif keyboard.is_pressed("z"):
            cursor_position()
        elif input.isnumeric():
            num = int(input)
            while num > 0:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1
    except:
        print("Input failed")
        break