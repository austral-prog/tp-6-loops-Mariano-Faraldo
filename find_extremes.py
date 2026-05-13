def find_min(numbers):
    menor = numbers[0]

    for numero in numbers:
        if numero < menor:
            menor = numero

    return menor


def find_max(numbers):
    mayor = numbers[0]

    for numero in numbers:
        if numero > mayor:
            mayor = numero

    return mayor


def count_negatives(numbers):
    cantidad = 0

    for numero in numbers:
        if numero < 0:
            cantidad += 1

    return cantidad