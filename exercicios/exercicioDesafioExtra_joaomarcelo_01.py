din = 93
total = 0
menor = int(din / 5)
maior = -1

while total != din:
  resto = int(din - (menor *5))
  total = menor * 5 + maior * 7
  if resto % 7 != 0:
    maior += 1
    menor -= 1

  print(maior)
  print(menor)
  
print(maior)
print(menor)
#13 alunos menores que 12
#4 alunos maiores que 12
