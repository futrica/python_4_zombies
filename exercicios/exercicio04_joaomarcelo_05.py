import string
texto = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""
lista = []
for c in string.punctuation:
    texto = texto.replace(c, ' ')
    
texto = texto.replace(',' , ' ').lower().rstrip().split()
x = 0

while x < len(texto):
    caractereFront = texto[x][0]
    caractereBack = texto[x][len(texto[x]) - 1] 
    if  caractereFront in "python" or caractereBack in "python":
        lista.append(texto[x])
    x+=1
        
print(lista)

cont = 0
y =0
while y < len(lista):
    if len(lista[y]) > 4:
        cont += 1
    y += 1

print("na lista 'python' tem %d palavras com + de 4 char" %cont)
    
