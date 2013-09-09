peso = float(input ("informe o peso: "))

excesso = 0
multa = 0
if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
print("ultrapassou %.2f quilos, deve pagar %.2f" %(excesso,multa))
    
