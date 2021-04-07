# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
def mínimo (lista):
    if len(lista)<=0:
        return False
    else:
        return min(lista)


# print(mínimo ([37,2,1, -9]))
print(mínimo ([]))