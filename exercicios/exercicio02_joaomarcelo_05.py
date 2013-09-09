num1 = int(input ("entre com o numero 1: "))
num2 = int(input ("entre com o numero 2: "))
num3 = int(input ("entre com o numero 3: "))

   
if (num1 > num2 and num1 >num3):
    maior = num1    
elif (num2 > num1 and num2 > num3):
    maior = num2
elif (num3 > num1 and num3>num2):
    maior = num3
else:
    print("ha numeros iguais")

if (num1 < num2 and num1 <num3):
    menor = num1    
elif (num2 < num1 and num2 < num3):
    menor = num2
elif (num3 < num1 and num3<num2):
    menor = num3

print("maior num é %d e o menor é %d" %(maior,menor))
