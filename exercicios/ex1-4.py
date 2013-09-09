#4) Faça um programa que calcule
#o aumento de um salário.
#Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

sal = float(input ("qual salario? "))
aum = float(input ("porcentagem: "))
sal += sal*aum/100
print("novo salario é: %.2f" %sal)
