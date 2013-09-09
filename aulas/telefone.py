#programa para calcular valores de minutos utilizados
#pycursos 2013
#author jmfutrica@gmail.com


min = float(input ("quantos min gastou?" ))
if min < 200:
    valor = min *0.2
else:
    if min > 200 and min <=  400:
        valor = min *0.18
    else:        
        if min <=  800:
            valor = min *0.15
        else:
            valor = min * 0.08
            
print("valor da conta %0.2f" %valor)    
            
