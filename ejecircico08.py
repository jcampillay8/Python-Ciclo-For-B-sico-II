# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}
def ultimate_analysis (lista):
    dic={'totalTotal': 0, 'promedio': 0, 'minimo': 0, 'maximo': 0, 'longitud': 0}
    dic['totalTotal']=sum(lista)
    dic['promedio']=sum(lista)/len(lista)
    dic['minimo']=min(lista)
    dic['maximo']=max(lista)
    dic['longitud']=len(lista)
    return dic


print(ultimate_analysis ([37,2,1, -9]))