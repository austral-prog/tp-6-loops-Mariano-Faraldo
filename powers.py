def power(base, exp):
    acomulador = 1
    for i in range(1, exp+1):
            acomulador = acomulador * base
    return acomulador


def sum_of_powers(base, max_exp):
    acomulador = 0
    for i in range(max_exp + 1):
        acomulador += power(base, i)
    return acomulador

