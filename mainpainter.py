import pyautogui
import keyboard
import random
from scipy.spatial import ConvexHull
import sys

# this program operates in a 1900 x 860 MS Paint canvas and visualises the convex hull problem with drawn nodes and edges given a number of randomly placed nodes
# (ctrl + 1): creates 10 random nodes and draws the convex hull edges
# (0-9): draws given number of random nodes on canvas
# (-): draws the edges of the convex hull problem nodes including all previously drawn nodes
# (z): outputs the coordinates of the cursor in terminal
# (esc): stops the program from running after completing its given task 

# size of 1900 x 860 MS Paint canvas (minus 5)
xmin = 10
xmax = 1894
ymin = 149
ymax = 993

coords = []

running = True

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


def exit_program(e):
    global running
    if e.name == "esc":
        print("Successful termination")
        running = False

keyboard.hook(exit_program)

while running:
    try:
        input = keyboard.read_key()
        if keyboard.is_pressed("-"):
            coords.sort()       # sorts based on x-coord and then y-coord
            connect_points()
        elif keyboard.is_pressed("z"):
            cursor_position()
        elif keyboard.is_pressed("ctrl+1"):
            num = 10
            while num > 0 and running:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1
            coords.sort()       # sorts based on x-coord and then y-coord
            connect_points()
            break
        elif input.isnumeric():
            num = int(input)
            while num > 0 and running:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1
    except:
        print("Input failed")
        break