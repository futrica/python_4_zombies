#9) Escreva um programa que pergunte a quantidade
#de km percorridos por um carro alugado pelo 
#usuário, assim como a quantidade de
#dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dia = int(input ("qtd de dias: "))
km = float(input ("qtd de km rodado: "))
preco = (dia * 60) + (km * 0.15)
print("total a pagar %.2f" %preco)
