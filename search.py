def index_of(target, lst):
    for i in range(len(lst)):
        valor = lst[i]
        if valor == target:
            return i
        
    return -1


def index_of_by_index(target, lst, start):
    for i in range(start, len(lst)):
        valor = lst[i]
        if valor == target:
            return i

    return -1

def index_of_empty(lst):
    for i in range(len(lst)):
        valores = lst[i]
        if valores == "":
            return i
        
    return -1
