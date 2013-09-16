def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)

#testando

palavra = input("entre com a string: ")
print(embaralha(palavra))
