valor = float(input ("valor compra: "))
cash = float(input ("valor pago: "))

resto =  cash - valor
troco = []
notas = [50,20, 10, 5 , 2 ,1]
i= 0

while (int(resto) >= 1 ):
    while( int(resto) >= notas[i]):
        troco.append(notas[i])
        resto = int(resto) - int(notas[i])
    i +=1

print(troco)
    
    
