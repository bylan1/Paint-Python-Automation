from algorithm import *
import keyboard

running = True

coords = [[15, 973], [1448, 457], [793,606], [1149, 323], [377, 505], [473, 312], [287, 797], [1224, 963]]

def exit_program(e):
    global running
    if e.name == "esc":
        print("Successful termination")
        running = False

keyboard.hook(exit_program)


while running:
    try:
        if keyboard.is_pressed('a'):
            coords.sort()
            print("Drawing lines...")
            connect_points(coords, 'voronoi')
        elif keyboard.is_pressed('s'):
            coords.sort()
            print("Drawing lines...")
            connect_points(coords, 'delaunay')
        elif keyboard.is_pressed('d'):
            coords.sort()
            print("Drawing lines...")
            connect_points(coords, 'convex_hull')
    except:
        print("Input failed")
        break