import pyautogui
import random
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay
from scipy.spatial import Voronoi

# size of 1900 x 860 MS Paint canvas (minus 5)
X_MIN = 10
X_MAX = 1894
Y_MIN = 149
Y_MAX = 993


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
    x = random.randint(X_MIN, X_MAX)
    y = random.randint(Y_MIN, Y_MAX)
    pyautogui.moveTo(x, y, duration=0)
    return [x, y]

# output cursors current position
def cursor_position():
    x, y = pyautogui.position()
    print(f"Current Cursor Position - X: {x}, Y: {y}")

def simplice_to_edge(simplices):
    edges = []
    for tri in simplices:
        for k in range(3):
            i, j = tri[k], tri[(k+1)%3]
            i, j = min(i,j), max(i, j)
            edges.append((i,j))
    
    return edges

# convex hull solution
def compute(a, problem):
    print("Computing...")
    points = [(x,y) for x, y in a]

    if problem == "delaunay":
        ret = Delaunay(points)
        edges = simplice_to_edge(ret.simplices)
        unique_points = []
        for (a, b) in edges:
            unique_points.append(a)
            unique_points.append(b)
        return [points[idx] for idx in unique_points]
    
    elif problem == "convex_hull":
        ret = ConvexHull(points)
        return [points[vertex] for vertex in ret.vertices]
    
    # incomplete voronoi method
    elif problem == "voronoi":
        ret = Voronoi(points)

        return [points[vertex] for vertex in ret.vertices]
    
    return None

# draws line connecting points in the drawing order
def connect_points(coords, problem):
    # print(coords)
    if len(coords) > 2:
        edge_points = compute(coords, problem)
        edge_points.append(edge_points[0])      # adds last point to loop convex hull
    else:
        edge_points = coords
    
    length = len(edge_points)

    # print(edge_points)

    edges = set([])

    for i in range(length):
        if i == 0:
            pyautogui.moveTo(edge_points[i][0], edge_points[i][1])
        else:
            if edge_points[i-1] == edge_points[i]:
                continue

            current_edge = (edge_points[i-1], edge_points[i])
            reverse_edge = (edge_points[i], edge_points[i-1])

            if problem == "delaunay" and (current_edge in edges or reverse_edge in edges or i % 2 == 0):
                pyautogui.moveTo(edge_points[i][0], edge_points[i][1])
            else:
                pyautogui.dragTo(edge_points[i][0], edge_points[i][1], duration=0.1, button="left")
                edges.add(current_edge)
                edges.add(reverse_edge)

