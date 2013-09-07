#5) Solicite o preço de uma mercadoria
#e o percentual de desconto.
#Exiba o valor do desconto e o
#preço a pagar.

merc = float(input ("valor mercadoria? "))
des = float(input ("porcentagem: "))
des = merc*des/100
merc -= des
print("desconto de: %.2f total a pagar: %.2f" %(des, merc))
