"""
Este módulo genera un laberinto y proporciona una interfaz gráfica usando Pygame. 
El laberinto es resuelto mediante un algoritmo de búsqueda recursiva. Incluye funcionalidades para:
- Mostrar el laberinto.
- Crear entradas, salidas y portales en posiciones aleatorias.
- Resolver el laberinto visualmente, considerando portales como atajos.
"""

import random
import pygame

WIDTH = 143
HEIGHT = 87
maze = {}
EMPTY = 0
WALL = 1
PORTAL1 = 3
PORTAL2 = 4

NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL

def showMaze(maze, screen, entrance, exit, path=[]):
    """
    Muestra el laberinto en la pantalla gráfica utilizando Pygame.
    
    Parámetros:
    - maze: Diccionario que contiene el estado actual del laberinto.
    - screen: La ventana de Pygame donde se dibuja el laberinto.
    - entrance: Coordenadas de la entrada del laberinto.
    - exit: Coordenadas de la salida del laberinto.
    - path: Lista opcional que contiene las posiciones del camino a seguir.
    """
    screen.fill(WHITE)
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
    pygame.draw.rect(screen, GREEN, (entrance[0] * 10, entrance[1] * 10, 10, 10))
    if exit:
        pygame.draw.rect(screen, YELLOW, (exit[0] * 10, exit[1] * 10, 10, 10))
    for x, y in path:
        if maze[(x, y)] not in [PORTAL1, PORTAL2] and (x, y) != entrance and (x, y) != exit:
            pygame.draw.rect(screen, RED, (x * 10, y * 10, 10, 10))
    pygame.display.flip()

def visit(x, y, screen, hasVisited):
    """
    Función recursiva que visita las celdas del laberinto generando caminos.
    
    Parámetros:
    - x, y: Coordenadas de la celda actual.
    - screen: Ventana gráfica de Pygame.
    - hasVisited: Lista de celdas ya visitadas para evitar volver a ellas.
    """
    maze[(x, y)] = EMPTY
    showMaze(maze, screen, (1, 1), None)
    pygame.event.pump()
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
            visit(nextX, nextY, screen, hasVisited)

def generateExitAndEntrance():
    """
    Genera una posición de entrada y salida aleatoria en los bordes del laberinto.
    
    Retorna:
    - exit: Coordenadas de la salida del laberinto.
    - entrance: Coordenadas de la entrada del laberinto.
    """
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
    """
    Coloca dos portales en posiciones aleatorias del laberinto. Los portales actúan como atajos.
    
    Retorna:
    - portal1: Coordenadas del primer portal.
    - portal2: Coordenadas del segundo portal.
    """
    portal1 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY])
    portal2 = random.choice([(x, y) for x in range(1, WIDTH, 2) for y in range(1, HEIGHT, 2) if maze[(x, y)] == EMPTY and (x, y) != portal1])
    maze[portal1] = PORTAL1
    maze[portal2] = PORTAL2
    return (portal1, portal2)

def solveMaze(screen, current, exit, path=[]):
    """
    Resuelve el laberinto utilizando un algoritmo recursivo de búsqueda.
    
    Parámetros:
    - screen: Ventana gráfica de Pygame.
    - current: Coordenadas actuales en el laberinto.
    - exit: Coordenadas de la salida del laberinto.
    - path: Lista que contiene el camino actual desde la entrada.
    
    Retorna:
    - True si encuentra una solución, False si no hay solución.
    """
    if current == exit:
        path.append(current)
        showMaze(maze, screen, entrance, exit, path)
        return True
    x, y = current
    path.append(current)
    pygame.event.pump()
    showMaze(maze, screen, entrance, exit, path)
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
                    return True
    path.pop()
    return False

def main():
    """
    Función principal que inicializa Pygame, genera el laberinto, las entradas, salidas y portales, y lo resuelve.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * 10, HEIGHT * 10))
    hasVisited = [(1, 1)]
    visit(1, 1, screen, hasVisited)
    global entrance
    exit, entrance = generateExitAndEntrance()
    global portals
    portals = generatePortals()
    solveMaze(screen, entrance, exit)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
