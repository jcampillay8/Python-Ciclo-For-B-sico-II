# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
def mínimo (lista):
    if len(lista)<=0:
        return False
    else:
        return max(lista)


print(mínimo ([37,2,1, -9]))
# print(mínimo ([]))