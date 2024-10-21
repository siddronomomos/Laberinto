import random

# Constants for maze properties
WIDTH = 143
HEIGHT = 87
maze = {}
EMPTY = 0
WALL = 1
PORTAL1 = 3
PORTAL2 = 4

# Directions for movement
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # For solving


# Initialize maze with walls
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL


def visit(x, y, hasVisited):
    maze[(x, y)] = EMPTY

    while True:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)
        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)
        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)
        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            return
        else:
            direction = random.choice(unvisitedNeighbors)
            if direction == NORTH:
                nextX, nextY = x, y - 2
                maze[(x, y - 1)] = EMPTY
            elif direction == SOUTH:
                nextX, nextY = x, y + 2
                maze[(x, y + 1)] = EMPTY
            elif direction == WEST:
                nextX, nextY = x - 2, y
                maze[(x - 1, y)] = EMPTY
            elif direction == EAST:
                nextX, nextY = x + 2, y
                maze[(x + 1, y)] = EMPTY

            hasVisited.append((nextX, nextY))
            visit(nextX, nextY, hasVisited)

def generateExitAndEntrance():
    edges = ['top', 'bottom', 'left', 'right']
    exit_edge = random.choice(edges)
    edges.remove(exit_edge)
    entrance_edge = random.choice(edges)

    if exit_edge == 'top':
        exit = (random.choice(range(1, WIDTH, 2)), 0)
    elif exit_edge == 'bottom':
        exit = (random.choice(range(1, WIDTH, 2)), HEIGHT - 1)
    elif exit_edge == 'left':
        exit = (0, random.choice(range(1, HEIGHT, 2)))
    elif exit_edge == 'right':
        exit = (WIDTH - 1, random.choice(range(1, HEIGHT, 2)))

    if entrance_edge == 'top':
        entrance = (random.choice(range(1, WIDTH, 2)), 0)
    elif entrance_edge == 'bottom':
        entrance = (random.choice(range(1, WIDTH, 2)), HEIGHT - 1)
    elif entrance_edge == 'left':
        entrance = (0, random.choice(range(1, HEIGHT, 2)))
    elif entrance_edge == 'right':
        entrance = (WIDTH - 1, random.choice(range(1, HEIGHT, 2)))

    maze[exit] = EMPTY  
    maze[entrance] = EMPTY 
    return exit, entrance

def generatePortals():
    portal1 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY])
    portal2 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY and (x, y) != portal1])
    maze[portal1] = PORTAL1
    maze[portal2] = PORTAL2

    return (portal1, portal2)

def solveMaze(current, exit, path=[]):
    if current == exit:
        path.append(current)
        return True 

    x, y = current
    path.append(current)



    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy

        if (nx, ny) in maze and maze[(nx, ny)] in [EMPTY, PORTAL1, PORTAL2] and (nx, ny) not in path:
            if maze[(nx, ny)] == PORTAL1:
                if solveMaze(portals[1], exit, path):
                    return True
            elif maze[(nx, ny)] == PORTAL2:
                if solveMaze(portals[0], exit, path):
                    return True
            else:
                if solveMaze((nx, ny), exit, path):
                    return True

    path.pop()
    return False

def main():

    hasVisited = [(1, 1)]
    visit(1, 1, hasVisited)

    global entrance
    exit, entrance = generateExitAndEntrance()

    # Generate portals
    global portals
    portals = generatePortals()

    # Solve the maze from entrance to exit

    # Main loop to keep the window open
    

import sys
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    main()
