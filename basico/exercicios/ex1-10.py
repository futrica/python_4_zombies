#10) Escreva um programa para  calcular a redução
#do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e
#quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

cig = int(input ("qts cigarros por dia? "))
ano = int(input ("a quanto anos fuma? "))
totFumado = (cig * ano * 365 * 24) /6 /24
print("dias de vida perdido de %d" %totFumado)
