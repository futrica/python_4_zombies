x = 0
letras = []
cons = 0

while(x < 10):
    letras.append(input ("entre com uma letra: "))
    x +=1
i=0
while( i <=9):
    if (letras[i] not in "aeiou"):
        cons += 1
    i +=1

print("foram lidas %d consoantes" %cons)


    
