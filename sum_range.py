def sum_to_n(n):
    if n <= 0:
        return 0
    acomulador = 0
    for i in range(1, n+1):
        acomulador = acomulador + i
    return acomulador



def sum_evens(n):
    if n <= 0:
        return 0
    acomulador = 0
    for i in range(2, n+1, 2):
        acomulador = acomulador + i
    return acomulador



def factorial(n):
    if n <= 0:
        return 1
    acomulador = 1
    for i in range(1,n+1):
        acomulador = acomulador * i
    return acomulador
