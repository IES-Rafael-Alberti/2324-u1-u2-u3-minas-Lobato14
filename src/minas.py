"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

def mostrarTablero(tablero, mostrar_minas=False):
    """
    Función que muestra el tablero    
    """
    filas = len(tablero)
    columnas = len(tablero[0])

    for fila in range(filas + 1):
        for columna in range(columnas + 1):
            if fila == 0 and columna == 0:
                print(' ', end=' ')
            elif fila == 0:
                print(columna, end=' ')
            elif columna == 0:
                print(fila, end=' ')
            else:
                if not mostrar_minas and tablero[fila - 1][columna - 1] == '*':
                    print('.', end=' ')
                else:
                    print(tablero[fila - 1][columna - 1], end=' ')
        print()

def mostrarMenu():
    """
    Función que muestra el menú del juego    
    """
    print("\n1. Revelar celda\n"+
    "2. Marcar celda\n"
    "3. Salir\n")
    return input("Elija una opcion: ")

def generarMinas(filas, columnas, tablero):
    """
    Función que genera minas aleatorias en el tablero
    """
    mina = "*"
    for _ in range(10):
        fila = random.randint(1, filas)
        columna = random.randint(1, columnas)
        if tablero[fila - 1][columna - 1] != mina:
            tablero[fila - 1][columna - 1] = mina
    return tablero

def contar_minas(tablero, fila, columna):
    """
    Función que cuenta el número de minas alrededor de una celda
    """
    mina = "*"
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0

    for i in range(max(1, fila - 1), min(filas, fila + 2)):
        for j in range(max(1, columna - 1), min(columnas, columna + 2)):
            if tablero[i - 1][j - 1] == mina:
                contador += 1

    return contador

def revelarCelda(tablero, fila, columna):
    """
    Función que revela una celda en el tablero
    """
    if tablero[fila - 1][columna - 1] == '.':
        minas_alrededor = contar_minas(tablero, fila, columna)
        tablero[fila - 1][columna - 1] = str(minas_alrededor) if minas_alrededor > 0 else ' '
        if minas_alrededor == 0:
            # Revelar celdas adyacentes si no hay minas alrededor
            for i in range(max(1, fila - 1), min(len(tablero), fila + 2)):
                for j in range(max(1, columna - 1), min(len(tablero[0]), columna + 2)):
                    if tablero[i - 1][j - 1] == '.':
                        revelarCelda(tablero, i, j)

def marcarCelda(tablero, fila, columna):
    """
    Función que marca una celda en el tablero
    """
    marcador_mina = "F"
    if tablero[fila - 1][columna - 1] == '.':
        tablero[fila - 1][columna - 1] = marcador_mina

def actualizarTablero(tablero, opcion, coordenadas, filas, columnas):
    """
    Función en la que actualiza el tablero en función de la opción seleccionada
    """
    fila, columna = coordenadas
    if 1 <= fila <= filas and 1 <= columna <= columnas:
        if opcion == '1':
            revelarCelda(tablero, fila, columna)
        elif opcion == '2':
            marcarCelda(tablero, fila, columna)
    else:
        print("Coordenadas fuera de rango. Vuelve a intentar.")

def revisarVictoria(tablero):
    """
    Función que revisa si todas las celdas sin minas han sido reveladas
    """
    for fila in tablero:
        for celda in fila:
            if celda == '.':
                return False
    return True

if __name__ == "__main__":
    
    filas = 8
    columnas = 8
    tablero = [['.' for _ in range(columnas)] for _ in range(filas)]

    opcion = ""
    generarMinas(filas, columnas, tablero)
    juego_en_curso = True

    while opcion != '3' and juego_en_curso:
        mostrarTablero(tablero)
        opcion = mostrarMenu()

        if opcion == '1' or opcion == '2':
            coordenadas_validas = False
            while not coordenadas_validas:
                coordenadas = input("Ingrese las coordenadas (fila, columna): ").split(',')
                if len(coordenadas) == 2 and coordenadas[0].isdigit() and coordenadas[1].isdigit():
                    coordenadas = (int(coordenadas[0]), int(coordenadas[1]))
                    coordenadas_validas = True
                else:
                    print("Coordenadas inválidas. Vuelve a intentar.")
            actualizarTablero(tablero, opcion, coordenadas, filas, columnas)
            if opcion == '1' and tablero[coordenadas[0] - 1][coordenadas[1] - 1] == '*':
                # Revelar todas las minas si el jugador revela una mina (pérdida)
                mostrarTablero(tablero, mostrar_minas=True)
                print("¡Has perdido!")
                juego_en_curso = False
            elif revisarVictoria(tablero):
                # Revisar si todas las celdas sin minas han sido reveladas (victoria)
                mostrarTablero(tablero, mostrar_minas=True)
                print("¡Has ganado!")
                juego_en_curso = False
        elif opcion != '3':
            print("Opción inválida.")

    print("¡Gracias por jugar!\n")