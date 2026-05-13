def enumerate_list(lst):
    resultado = []
    indice = 0
    for palabra in lst:
        if palabra != "":
            resultado.append(f"{indice}. {palabra}")
            indice += 1

    return resultado


def enumerate_backwards(lst):
    resultado = []
    indice = 0

    for palabra in lst:
        if palabra != "":
            palabra_invertida = palabra[::-1]
            resultado.append(f"{indice}. {palabra_invertida}")
            indice += 1

    return resultado