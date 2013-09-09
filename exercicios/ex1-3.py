#3) Escreva um programa que leia a
#quantidade de dias, horas,
#minutos e segundos do usuário. Calcule 
#o total em segundos.


dias = float(input ("dias: "))
horas = float (input ("horas: "))
minu = float (input ("minutos: ")) 
seg = (dias * 86400) + (horas * 3600) + (minu * 60)
print('convertendo %.2f dias + %.2f horas + %.2f minutos para segundos: %.2f segundos' %(dias, horas, minu, seg))
