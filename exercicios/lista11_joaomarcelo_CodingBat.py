# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# ExercÃ­cios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string jÃ¡ termine em 'ing', acrescentarÃ¡ 'ly'.
def verbing(s):
   if len(s) < 3:
      return s
   elif s[-1] == 'g' and s[-2] == 'n' and s[-3] == 'i':
      s = s + 'ly'  
   else:
      s = s + 'ing'
   return s

# H. not_bad
# Dada uma string, procura a primeira ocorrÃªncia de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  pos_bad = s.find('bad')
  pos_not = s.find('not')
  if pos_bad > pos_not:
    s =s.replace('bad', 'good')
    pos_good = s.find('good')    
    return s[0 : pos_not]  +  s[(pos_good) : len(s)]
  else:
    return s

# I. inicio_final
# Divida cada string em dois pedaÃ§os.
# Se a string tiver um nÃºmero Ã­mpar de caracteres
# o primeiro pedaÃ§o terÃ¡ um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final
def inicio_final(a, b):
  if (len(a)%2) == 0:
    meio = int(len(a) /2)     
    a1 = a[0:meio]
    a2 = a[(meio ):]
  else:
    meio = int(len(a) /2) + 1
    a1 = a[0:meio]
    a2 = a[(meio ):]
    
  if (len(b)%2) == 0:
    meio = int(len(b) /2)
    b1 = b[0:meio]
    b2 = b[(meio):]
  else:
    meio = int(len(b) /2) + 1
    b1 = b[0:meio]
    b2 = b[(meio):]

  return a1 + b1 + a2 + b2

# J. zeros finais
# Verifique quantos zeros hÃ¡ no final de um nÃºmero inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui trÃªs
def zf(n):
  cont = 0
  x = -1
  s =  str(n)
  c = True
  while c :
    if s[x] == '0':
      cont += 1
    else:
      c = False
    x -= 1
  return cont
    



# K. conta 2
# Verifique quantas vezes o dÃ­gito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dÃ­gito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  i = 0
  cont =0
  while i < n-1:
    num = str(i)
    k = 0
    while k < len(num):      
      if num[k] == '2':
        cont +=1
      k +=1
    i += 1
  return cont

# L. inicio em potencia de 2
# Dado um nÃºmero inteiro positivo n retorne a primeira potÃªncia de 2
# que tenha o inÃ­cio igual a n
# Exemplo: para n = 65 retornarÃ¡ 16 pois 2**16 = 65536
def inip2(n):
  cont = 0
  pot =1
  res = 0
  while n != res:
    pot = pot *2
    res = int(str(pot)[0:(len(str(n)))]) 
    cont +=1
  return cont

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print ()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ()
  print ('inicio_final')
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)

  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)

  print ()
  print ('inicio p2')
  test(inip2(7), 46)
  test(inip2(133), 316)
  test(inip2(1024), 10)
  
if __name__ == '__main__':
  main()
