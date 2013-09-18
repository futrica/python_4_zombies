import random
vetor1 = []
vetor2 = []
vetor3 = []
x= 0
for x in range(10):
    num= random.randint(1 ,100)
    vetor1.append(num)
    num = random.randint(1 ,100)
    vetor2.append(num)
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
    x +=1

print(vetor1, vetor2, vetor3)


    
