# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverse_list (lista):
    contador =0
    for i in range(len(lista)-1,-1,-1):        
        if contador<(len(lista)-1)/2:
            # print("hola")
            temp=lista[contador]
            lista[contador]=lista[len(lista)-1-contador]
            lista[len(lista)-1-contador]=temp
            contador+=1

        
    print(lista)

# print(reverse_list ([37,2,1, -9]))
reverse_list ([37,2,1, -9])