
import random
def crear_laberinto():
    laberinto = []
    for i in range(10):
        if i == 0:
            laberinto.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            continue
        elif i == 9:
            laberinto.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            continue
        laberinto.append([])
        for j in range(10):
            laberinto[i].append(random.choice([0, 1]))
            if j == 0 or j == 9:
                laberinto[i][j] = 1
                continue

    xexit = random.randint(0, 9)
    yexit = 0
    if xexit == 0 or xexit == 9:
        yexit = random.randint(0, 9)
    else :
        yexit = random.choice([0, 9])
    laberinto[yexit][xexit] = 2
        
    return laberinto

def imprimir_laberinto(laberinto):
    for i in range(10):
        for j in range(10):
            if laberinto[i][j] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def main():
    laberinto = crear_laberinto()
    imprimir_laberinto(laberinto)

if __name__ == "__main__":
    main()