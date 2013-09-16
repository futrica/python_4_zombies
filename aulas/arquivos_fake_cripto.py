with open("mensagem.txt") as f:
    arquivo = open("cripto.txt" , "w")
    lista = list(f.read().rstrip())
    for x in lista:        
        if x in "aeiou":
            arquivo.write('*')
        else:
            arquivo.write(x)
            
arquivo.close()
    
