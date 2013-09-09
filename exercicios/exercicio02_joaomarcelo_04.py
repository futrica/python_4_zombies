num1 = int(input ("entre com o numero 1: "))
num2 = int(input ("entre com o numero 2: "))
num3 = int(input ("entre com o numero 3: "))

   
if (num1 > num2 and num1 >num3):
    print("o num %d é maior" %num1)
elif (num2 > num1 and num2 > num3):
    print("o num %d é maior" %num2)
elif (num3 > num1 and num3>num2):
    print("o num %d é maior" %num3)
else:
    print("ha numeros iguais")
