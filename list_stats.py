def find_min(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


def find_max(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


def range_of(numbers):
    minimo = find_min(numbers)
    maximo = find_max(numbers)

    return maximo - minimo


def average(numbers):
    if len(numbers) == 0:
        return 0.0

    suma = 0

    for numero in numbers:
        suma += numero

    promedio = suma / len(numbers)

    return round(promedio, 1)


def describe(numbers):
    if len(numbers) == 0:
        return "Empty list"

    minimo = find_min(numbers)
    maximo = find_max(numbers)
    rango = range_of(numbers)
    promedio = average(numbers)

    return f"Min:{minimo} Max:{maximo} Range:{rango} Avg:{promedio}"