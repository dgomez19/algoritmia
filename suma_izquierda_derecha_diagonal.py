# Sumar la diagonal izquierda y diagonal derecha, restar izquierda - derecha ese es el resultado

def suma_diagonales(lista):
    suma_derecha = [lista[i][i] for i in range(len(lista))]

    suma_izquierda = [lista[len(lista) - 1 - i][i] for i in range(len(lista))]

    resultado = sum(suma_izquierda) - sum(suma_derecha)

    return resultado

lista = [[5, 1, 20], [4, 1, 6], [1, 8, 8]]

resultado = suma_diagonales(lista)
print(resultado)
