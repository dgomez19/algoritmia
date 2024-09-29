def bubble_sort(lista):
    n = len(lista) - 1

    for i in range(n):
        for j in range(n-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista
# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
numeros_ordenados = bubble_sort(numeros)
print("Lista ordenada:", numeros_ordenados)
