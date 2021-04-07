# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def sum_total (lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma/len(lista)


print(sum_total ([1,2,3,4]))

# print(sum_total ([6,3, -2]))