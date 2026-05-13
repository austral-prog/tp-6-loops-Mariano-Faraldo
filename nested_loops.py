def flatten(matrix):
    resultado = []

    for fila in matrix:
        for valor in fila:
            resultado.append(valor)

    return resultado


def row_sums(matrix):
    resultado = []

    for fila in matrix:
        suma = 0

        for valor in fila:
            suma += valor

        resultado.append(suma)

    return resultado


def col_sums(matrix):
    resultado = []

    for columna in range(len(matrix[0])):
        suma = 0

        for fila in range(len(matrix)):
            suma += matrix[fila][columna]

        resultado.append(suma)

    return resultado