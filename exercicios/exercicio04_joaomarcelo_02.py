import random
listaPar = []
listaImpar = []
while len(listaPar) + len(listaImpar) < 20:
    num = random.randint(1,100)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(listaPar)
print(listaImpar)
