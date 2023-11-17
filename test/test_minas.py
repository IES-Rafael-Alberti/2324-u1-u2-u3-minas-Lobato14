from src.minas import (
    generar_minas,
    contar_minas_alrededor,
    revelar_celda,
    marcar_celda,
    actualizar_tablero,
    revisar_victoria,
)

# Test para generar minas
def test_generar_minas():
    filas = 8
    columnas = 8
    tablero = [['.' for _ in range(columnas)] for _ in range(filas)]
    # Prueba que la función no genere ninguna mina antes de invocar generar_minas
    assert sum(fila.count('*') for fila in tablero) == 0
    # Genera las minas
    tablero_con_minas = generar_minas(filas, columnas, tablero)
    # Prueba que la función haya generado el número correcto de minas
    assert sum(fila.count('*') for fila in tablero_con_minas) == 10
    # Prueba que las posiciones de las minas estén dentro del rango del tablero
    for fila in range(filas):
        for celda in range(columnas):
            if tablero_con_minas[fila][celda] == '*':
                assert 1 <= fila + 1 <= filas
                assert 1 <= celda + 1 <= columnas

# Test para contar las minas al rededor
def test_contar_minas_alrededor():
    tablero = [
        ['.', '.', '.'],
        ['*', '*', '*'],
        ['.', '.', '.']
    ]
    assert contar_minas_alrededor(tablero, 2, 2) == 8

# Test para revelar la celda
def test_revelar_celda():
    tablero = [
        ['.', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ]
    revelar_celda(tablero, 1, 1)
    assert tablero == [
        ['1', ' ', ' '],
        [' ', '*', ' '],
        [' ', ' ', ' ']
    ]

# Test para marcar una posible mina
def test_marcar_celda():
    tablero = [
        ['.', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ]

    marcar_celda(tablero, 1, 1)
    assert tablero == [
        ['F', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ]

# Test para actualizar el tablero y que se revele la celda
def test_actualizar_tablero_revelar_celda():
    tablero = [
        ['.', '.', '.'],
        ['.', '*', '.'],
        ['.', '.', '.']
    ]
    actualizar_tablero(tablero, '1', (1, 1), 3, 3)
    assert tablero == [
        ['1', ' ', '.'],
        [' ', '*', '.'],
        [' ', ' ', ' ']
    ]

# Test para revisar la victoria con minas pendientes

def test_revisar_victoria_con_minas_pendientes():
    tablero_con_minas = [
        ['1', '2', '1'],
        ['*', '*', '*'],
        ['2', '*', '2']
    ]
    assert revisar_victoria(tablero_con_minas)