def duplicados(lista):


    no_duplicados = {}
    print('lista', sorted(set(lista)))

    for i in lista:
        no_duplicados[i] = i

    print('i', no_duplicados.keys())





lista = [10, 20, 10, 50, 40, 20, 10, 50, 100, 800, 40]

resultado = duplicados(lista)
print(resultado)