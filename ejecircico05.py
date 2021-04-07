# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def longitud (lista):
    contar=0
    for i in range(len(lista)):
        contar+=1
    return contar


# print(longitud ([37,2,1, -9]))
print(longitud ([]))