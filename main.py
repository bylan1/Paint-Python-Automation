import keyboard
from algorithm import *


# this program operates in a 1900 x 860 MS Paint canvas and visualises the convex hull problem with drawn nodes and edges given a number of randomly placed nodes
# (ctrl + 1): creates 10 random nodes and draws the convex hull edges
# (0-9): draws given number of random nodes on canvas
# (,): draws the edges of the delauney triangulation nodes including all previously drawn nodes
# (.): draws the edges of the convex hull problem nodes including all previously drawn nodes
# (/): draws the edges of the voronoi diagram nodes including all previously drawn nodes
# (z): outputs the coordinates of the cursor in terminal
# (esc): stops the program from running after completing its given task 

running = True

coords = [[52, 269], [601, 695], [1305, 903], [1504, 177], [1859, 779]]

def exit_program(e):
    global running
    if e.name == "esc":
        print("Successful termination")
        running = False

keyboard.hook(exit_program)


while running:
    try:
        input = keyboard.read_key()
        if keyboard.is_pressed(","):
            coords.sort()       # sorts based on x-coord and then y-coord
            print("Drawing lines...")
            connect_points(coords, "delaunay")
        elif keyboard.is_pressed("."):
            coords.sort()
            print("Drawing lines...")
            connect_points(coords, "convex_hull")
        elif keyboard.is_pressed("/"):
            coords.sort()
            print("Drawing lines...")
            connect_points(coords, "voronoi")
        elif keyboard.is_pressed("z"):
            cursor_position()
        elif keyboard.is_pressed("ctrl+1"):
            num = 10
            while num > 0 and running:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1

            if not running:
                break
            
            coords.sort()       # sorts based on x-coord and then y-coord
            connect_points(coords, "convex_hull")
            continue
        elif input.isnumeric():
            num = int(input)
            print("Drawing circles...")
            while num > 0 and running:
                coords.append(random_cursor())
                cursor_position()
                circle_draw()
                num -= 1

    except:
        print("Input failed")
        break