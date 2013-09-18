import random
lista = []
while len(lista) < 10:
    num = random.randint(1,100)
    if num not in lista:
        lista.append(num)
lista.sort()
print(lista)
print("maior num: %d" %lista[9])
print("menor num: %d" %lista[0])
        
    
