def binary_search(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = int((alto + baixo)/2)
        tentativa = lista[meio]
        if tentativa == item:
            return meio
        elif tentativa > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
