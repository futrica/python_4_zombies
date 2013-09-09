x = 0
lista = []
while(x < 10):
    n = int(input ("entre com o num: "))
    lista.append(n)
    x +=1

while(x > 0):
    print(lista[x-1])
    x -= 1
