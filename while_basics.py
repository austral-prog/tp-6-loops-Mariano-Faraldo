def countdown(n):
    if n < 0:
        return []

    numeros = []

    while n >= 0:
        numeros.append(n)
        n -= 1

    return numeros


def double_until(limit):
    if limit < 1:
        return []

    numeros = []
    valor = 1

    while valor <= limit:
        numeros.append(valor)
        valor *= 2

    return numeros