# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def count_positives (lista):
    contar=0
    for i in range(len(lista)):
        if lista[i] > 0:
            contar+=1
    lista[len(lista)-1]=contar
    return lista



# print(count_positives ([- 1,1,1,1]))
print(count_positives ([1,6, -4, -2, -7, -2]))