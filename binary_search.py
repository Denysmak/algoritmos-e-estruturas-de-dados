def busca_binaria(lista, item):
    alto = len(lista) - 1
    baixo = 0
    while baixo <= alto:
        meio = (alto + baixo) //2
        chute = lista[meio]
        if chute > item:
            baixo = meio + 1 
        elif chute < item:
            alto = meio - 1
        else:
            return meio


