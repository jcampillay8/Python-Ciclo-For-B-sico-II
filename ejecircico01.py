# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def biggie_size (lista):
    for i in range(len(lista)):
        if lista[i]>0:
            lista[i]="big"
    
    return lista

print(biggie_size ([- 1, 3, 5, -5]))