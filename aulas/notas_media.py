x = 0
notas = []
acum = 0
while(x < 4):
    n = float(input ("entre com o num: "))
    acum += n 
    notas.append(n)
    x +=1

print(notas)
print("media de ", (acum/4))
