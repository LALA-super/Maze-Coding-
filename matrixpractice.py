import random

def find_positions(laby):
    pos_p = None
    monsters = []

    rows = len(laby)
    columns = len(laby[0])

    for i in range(rows):
        for j in range(columns):
            if laby[i][j] == "P":
                pos_p = (i, j)
            elif laby[i][j] == "M":
                monsters.append((i, j))

    return pos_p, monsters



def print_labyrinth(laby):
    for rows in laby:
        line = ""
        for element in rows:
            if element == 1:
                line += "1 " 
            elif element == "P":
                line +=  "P " 
            elif element == "M":
                line += "M "
            elif element == "S":
                line += "S "
            else:
                line += str(element) + " "
        print(line)
    print()


# -----------------------------
# Starting Labyritnth 
# -----------------------------
laby = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, "M", 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, "P", 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, "S", 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, "M", 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, "M", 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

(pos_i, pos_j), monster = find_positions(laby)

lives = 3
turn = 0  

moves = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1)
}

jugando = True

print("Labyritnh Game")
print("monsters will move randomly")
print_labyrinth(laby)


while jugando:
    print("lives:", lives)
    mov = input("Mover (w/a/s/d) o 'x' para salir: ")

    if mov == "x":
        print("end of game.")
        jugando = False
    else:
        # Validación del movimiento sin usar "in"
        try:
            di, dj = moves[mov]
            movimiento_valido = True
        except KeyError:
            movimiento_valido = False

        if movimiento_valido:
            ni = pos_i + di
            nj = pos_j + dj
            casilla = laby[ni][nj]

            # 1) Chocar contra pared
            if casilla == 1:
                vidas -= 1
                print("Has chocado contra una pared. Pierdes una vida.")
                if vidas == 0:
                    print("Te quedaste sin vidas.")
                    jugando = False

            # 2) Llegar a salida
            elif casilla == "S":
                laby[pos_i][pos_j] = 0
                laby[ni][nj] = "P"
                #imprimir_laberinto(lab)
                print("¡Has ganado!")
                jugando = False

            # 3) Encontrar al monstruo
            elif casilla == "M":
                print("El monstruo te ha atrapado. Teletransporte aleatorio...")
                laby[pos_i][pos_j] = 0

                encontrada = False
                while encontrada == False:
                    filas = len(laby)
                    columnas = len(laby[0])
                    '''
                    random.randint(a, b):
                    - Genera un número entero aleatorio entre a y b.
                    - Incluye tanto a como b.
                    - Lo usamos para elegir una posición aleatoria dentro del laberinto.
                    '''
                    tele_i = random.randint(1, filas - 2)
                    tele_j = random.randint(1, columnas - 2)
                    if laby[tele_i][tele_j] == 0:
                        encontrada = True
                '''
                pos_i = tele_i
                pos_j = tele_j
                '''
                pos_i, pos_j = tele_i, tele_j
                laby[pos_i][pos_j] = "P"
                #imprimir_laberinto(lab)

            # 4) Casilla normal
            else:
                laby[pos_i][pos_j] = 0
                laby[ni][nj] = "P"
                '''
                pos_i = ni
                pos_j = nj
                '''
                pos_i, pos_j = ni, nj
                #imprimir_laberinto(lab)

            # ----------------------------
            # MOVIMIENTO DE TODOS LOS MONSTRUOS
        if turn % 2 == 0:  # Cada 2 turnos

            new_monsters = []

            for (mon_i, mon_j) in monster:
                '''
                list(movs.values()):
                - Obtiene todos los valores del diccionario 'movs'.
                - Cada valor es un desplazamiento (di, dj) para moverse.
                - Lo convertimos a lista para poder recorrerlo o elegir un movimiento aleatorio.
                '''
                # 4 direcciones
                direcciones = list(moves.values())
                posibles = []

                for d in direcciones:
                    mi = mon_i + d[0]
                    mj = mon_j + d[1]

                    # Solo mover si es un camino vacío
                    if laby[mi][mj] == 0:
                        posibles.append((mi, mj))

                # Elegir movimiento aleatorio si existe
                if len(posibles) > 0:
                    '''
                    random.choice(posibles):
                    - 'posibles' es una lista con todas las casillas a las que el monstruo puede moverse.
                    - random.choice() selecciona una de esas casillas al azar.
                    - Guardamos esa casilla en 'elegido' para mover el monstruo allí.
                    '''
                    elegido = random.choice(posibles)
                    nuevo_i, nuevo_j = elegido

                    laby[mon_i][mon_j] = 0
                    laby[nuevo_i][nuevo_j] = "M"

                    new_monsters.append((nuevo_i, nuevo_j))
                else:
                    # Monstruo sin movimiento
                    new_monsters.append((mon_i, mon_j))

            monster = new_monsters
            print_labyrinth(laby)




        else:
            print("Movimiento no válido.")