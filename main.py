import random
import pygame
import time

# Constants for maze properties
WIDTH = 101
HEIGHT = WIDTH
maze = {}
EMPTY = 0
WALL = 1
PORTAL1 = 3
PORTAL2 = 4

# Directions for movement
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # For solving

# Colors for rendering
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)   # Entrance
YELLOW = (255, 255, 0) # Exit
RED = (255, 0, 0)     # Path
BLUE = (0, 0, 255)    # Portal 1
ORANGE = (255, 165, 0) # Portal 2

# Initialize maze with walls
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL

def showMaze(maze, screen, entrance, exit, path=[]):
    """Render the maze with entrance, exit, and optional path."""
    screen.fill(WHITE)

    # Draw walls and empty spaces
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[(x, y)] == EMPTY:
                color = WHITE
            elif maze[(x, y)] == WALL:
                color = BLACK
            elif maze[(x, y)] == PORTAL1:
                color = BLUE
            elif maze[(x, y)] == PORTAL2:
                color = ORANGE
            pygame.draw.rect(screen, color, (x * 10, y * 10, 10, 10))

    # Draw entrance and exit
    pygame.draw.rect(screen, GREEN, (entrance[0] * 10, entrance[1] * 10, 10, 10))
    if exit:
        pygame.draw.rect(screen, YELLOW, (exit[0] * 10, exit[1] * 10, 10, 10))

    # Draw the path in red, but avoid portals
    for x, y in path:
        if maze[(x, y)] not in [PORTAL1, PORTAL2]:
            pygame.draw.rect(screen, RED, (x * 10, y * 10, 10, 10))

    pygame.display.flip()

def visit(x, y, screen, hasVisited):
    """Recursive maze generation using DFS."""
    maze[(x, y)] = EMPTY
    showMaze(maze, screen, (1, 1), None)  # Display updates during generation
    pygame.event.pump()  # Handle event queue to prevent crashing
    #time.sleep(0.01)  # Add a small delay to make updates visible

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
            return  # Maze generation complete
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
            visit(nextX, nextY, screen, hasVisited)

def generateExitAndEntrance():
    """Generate a random exit on the outer edge of the maze and an entrance on a different side."""
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

    maze[exit] = EMPTY  # Ensure exit is on a path
    maze[entrance] = EMPTY  # Ensure entrance is on a path
    return exit, entrance

def generatePortals():
    """Generate one pair of portals in the maze."""
    portal1 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY])
    portal2 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY and (x, y) != portal1])
    maze[portal1] = PORTAL1
    maze[portal2] = PORTAL2

    return (portal1, portal2)

def solveMaze(screen, current, exit, path=[]):
    if current == exit:
        path.append(current)  # Add the exit to the path
        showMaze(maze, screen, entrance, exit, path)  # Display the final path
        return True  # Maze solved

    x, y = current
    path.append(current)  # Add current position to the path
    pygame.event.pump()  # Handle event queue to prevent crashing
    showMaze(maze, screen, entrance, exit, path)  # Display updates during solving
    #time.sleep(0.01)  # Delay for visualization

    # Explore neighbors in all four directions
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy

        if (nx, ny) in maze and maze[(nx, ny)] in [EMPTY, PORTAL1, PORTAL2] and (nx, ny) not in path:
            if maze[(nx, ny)] == PORTAL1:
                if solveMaze(screen, portals[1], exit, path):
                    return True
            elif maze[(nx, ny)] == PORTAL2:
                if solveMaze(screen, portals[0], exit, path):
                    return True
            else:
                if solveMaze(screen, (nx, ny), exit, path):
                    return True  # Path to exit found

    path.pop()  # Backtrack if no path found
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * 10, HEIGHT * 10))

    # Generate maze starting from (1, 1)
    hasVisited = [(1, 1)]
    visit(1, 1, screen, hasVisited)

    # Generate a random exit on the maze's outer edge and an entrance on a different side
    global entrance
    exit, entrance = generateExitAndEntrance()

    # Generate portals
    global portals
    portals = generatePortals()

    # Solve the maze from entrance to exit
    solveMaze(screen, entrance, exit)

    # Main loop to keep the window open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

import sys
sys.setrecursionlimit(10**6)
import threading
threading.stack_size(2**26)
threading.Thread(target=main).start()
