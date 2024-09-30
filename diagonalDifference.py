# def diagonalDifference(arr):
#     # Write your code here
#     suma_derecha = 0
#     for i in range(len(arr)):
#         suma_derecha += arr[i][i]
    
#     suma_izquierda = [arr[i][n - 1 - i] for i in range(len(arr))]

#     return sum(suma_izquierda) - suma_derecha



def diagonalDifference(arr):
    suma_derecha = [arr[i][i] for i in range(len(arr))]

    n = len(arr)

    suma_izquierda = [arr[i][n - 1 - i] for i in range(len(arr))]

    return sum(suma_izquierda) - sum(suma_derecha)


arr = [[5, 1, 20], [4, 1, 6], [1, 8, 8]]
result = diagonalDifference(arr)
print(result)
