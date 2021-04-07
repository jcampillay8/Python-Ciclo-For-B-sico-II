# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sum_total (lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma


# print(sum_total ([1,2,3,4]))

print(sum_total ([6,3, -2]))