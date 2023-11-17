"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random


def mostrar_tablero(tablero:list, mostrar_minas: bool = False) -> None:
    """
    Función que muestra el tablero del buscaminas

    Parameters
    ----------
    - tablero : list
        Es una lista de listas que representa el estado actual del tablero.
    - mostrar_minas : bool
        Indica si las minas deben mostrarse en el tablero. Por defecto es False.
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

def mostrar_menu() -> str:
    """
    Muestra el menú del juego de buscaminas y solicita al usuario que elija una opción.

    Returns
    -------
    - str: 
        La opción seleccionada por el usuario.
    """
    print("\n1. Revelar celda\n"
          "2. Marcar celda\n"
          "3. Salir\n")
    return input("Elija una opcion: ")


def generar_minas(filas: int, columnas: int, tablero: list[list[str]]) -> list[list[str]]:
    """
    Genera minas aleatorias en el tablero del juego de buscaminas.

    Parameters
    ----------
    - filas : int 
        Número de filas del tablero.
    - columnas : int
        Número de columnas del tablero.
    - tablero : list[list[str]]
        Matriz que representa el tablero del juego.

    Returns
    -------
    - list[list[str]]
        El tablero con las minas generadas.
    """
    mina = "*"
    for _ in range(10):
        fila_mina = random.randint(1, filas)
        columna_mina = random.randint(1, columnas)
        if tablero[fila_mina - 1][columna_mina - 1] != mina:
            tablero[fila_mina - 1][columna_mina - 1] = mina
    return tablero

def contar_minas_alrededor(tablero:list[list[str]], fila: int, columna:int) -> int:
    """
    Función que cuenta el número de minas alrededor de una celda en el tablero 
    del buscaminas.

    Parameters
    ----------
    - tablero : list[list[str]]
        Matriz que representa el tablero del juego.
    - fila : int
        Fila de la celda en el tablero.
    - columna : int
        Columna de la celda en el tablero.

    Returns
    --------
    - int: 
        Número de minas alrededor de la celda.
    """
    mina = "*"
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0

    for fila_adyacente in range(max(1, fila - 1), min(filas, fila + 2)):
        for columna_adyacente in range(max(1, columna - 1), min(columnas, columna + 2)):
            if tablero[fila_adyacente - 1][columna_adyacente - 1] == mina:
                contador += 1
    return contador

def revelar_celda(tablero:list[list[str]], fila:int, columna:int) -> None:
    """
    Función que revela una celda en el tablero del buscaminas

    Parameters
    ----------
    - tablero : list[list[str]]
        Matriz que representa el tablero del juego.
    - fila : int 
        Fila de la celda a revelar.
    - columna : int 
        Columna de la celda a revelar.
    """
    if tablero[fila - 1][columna - 1] == '.':
        minas_alrededor = contar_minas_alrededor(tablero, fila, columna)
        tablero[fila - 1][columna - 1] = str(minas_alrededor) if minas_alrededor > 0 else ' '
        if minas_alrededor == 0:
            # Revelar celdas adyacentes si no hay minas alrededor
            for fila_adyacente in range(max(1, fila - 1), min(len(tablero), fila + 2)):
                for columna_adyacente in range(max(1, columna - 1), min(len(tablero[0]), columna + 2)):
                    if tablero[fila_adyacente - 1][columna_adyacente - 1] == '.':
                        revelar_celda(tablero, fila_adyacente, columna_adyacente)

def marcar_celda(tablero:list[list[str]], fila:int, columna:int) -> None:
    """
    Marca una celda en el tablero del buscaminas.

    Parameters
    ----------
    - tablero: list[list[str]]
        Matriz que representa el tablero del juego.
    - fila : int
        Fila de la celda a marcar.
    - columna : int
        Columna de la celda a marcar.
    """
    marcador_mina = "F"
    if tablero[fila - 1][columna - 1] == '.':
        tablero[fila - 1][columna - 1] = marcador_mina

def actualizar_tablero(tablero:list[list[str]], opcion:str, coordenadas:tuple[int, int], 
                       filas:int, columnas:int) -> str:
    """
    Función que actualiza el tablero en función de la opción seleccionada.

    Parameters
    ----------
    - tablero : list[list[str]]
        Matriz que representa el tablero del juego.
    - opcion : str
        Opción que se vaya a introducir
    - coordenadas : tuple[int, int]:
        Coordenadas de la celda a actualizar.
    - filas : int
        Número de filas del tablero.
    - columnas : int 
        Número de columnas del tablero.

    Returns
    --------
    - str: 
        Mensaje de error si las coordenadas están fuera de rango o si se introduce una letra, 
        None si todo está correcto.
    """
    fila, columna = coordenadas
    try:
        fila, columna = int(fila), int(columna)
        if not (1 <= fila <= filas and 1 <= columna <= columnas):
            raise ValueError("Coordenadas fuera de rango. Vuelve a intentar.")
        if opcion == '1':
            revelar_celda(tablero, fila, columna)
        elif opcion == '2':
            marcar_celda(tablero, fila, columna)
        return None
    except ValueError:
        return "Coordenadas inválidas. Vuelve a intentar."

def revisar_victoria(tablero:list[list[str]]) -> bool:
    """
    Función que revisa si todas las celdas sin minas han sido reveladas

    Parameters
    ----------
    - tablero : list[List[str]]
        Matriz que representa el tablero del juego.

    Returns
    -------
    - bool: 
        True si todas las celdas sin minas han sido reveladas, False en caso contrario.
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
    generar_minas(filas, columnas, tablero)
    juego_en_curso = True

    while opcion != '3' and juego_en_curso:

        mostrar_tablero(tablero)
        opcion = mostrar_menu()

        if opcion == '1' or opcion == '2':

            coordenadas_validas = False

            while not coordenadas_validas:
                coordenadas = input("Ingrese las coordenadas (fila, columna): ").split(',')
                error_message = actualizar_tablero(tablero, opcion, coordenadas, filas, columnas)
                if error_message:
                    print(error_message)
                else:
                    coordenadas_validas = True

            if opcion == '1' and tablero[int(coordenadas[0]) - 1][int(coordenadas[1]) - 1] == '*':
                # Revelar todas las minas si el jugador revela una mina
                # en caso de que pierda
                mostrar_tablero(tablero, mostrar_minas=True)
                print("¡Has perdido!")
                juego_en_curso = False
            elif revisar_victoria(tablero):
                # Revisar si todas las celdas sin minas han sido reveladas
                # en caso de que haya conseguido la victoria
                mostrar_tablero(tablero, mostrar_minas=True)
                print("¡Has ganado!")
                juego_en_curso = False
        elif opcion != '3':
            print("Opción inválida.")
    print("¡Gracias por jugar!\n")