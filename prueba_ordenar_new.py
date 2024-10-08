# Dada una lista en desorden, devuelva la lista de forma ordenada


def ordenar_lista(lista):

    sorted(lista, reverse=False) # Ordenamiento normal

    # Ordenamiento aplicando bucles
    for _ in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j + 1] > lista[j]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]

    return lista


lista = [100, 10, 150, 20, 80, 30] # Se espera como respuesta [10, 20, 30, 80, 100, 150]

lista_descendente = ordenar_lista(lista)
print(lista_descendente)
