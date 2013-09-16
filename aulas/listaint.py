def listaInt(x , y):
    import random
    lista = []
    x = 0
    for i in range(15):
        lista.append(random.randint(x,y))
    return lista

#testando
print(listaInt(10, 100))
