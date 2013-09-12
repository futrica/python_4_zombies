#Dizemos que um número natural é  triangular se ele é produto
# de três números naturais
#consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120.
#Dado um inteiro não-negativo  n, 
#verificar se n é triangular.

n = int(input ("digite um numero: "))

res = 0
i = 1
while( i < n/3):
    res = i * (i + 1) * (i +2)
    if res == n:
        print("numero %d é triangular" %n)
        break
    i +=1

if res != n:
    print("numero %d não é triangular" %n)
