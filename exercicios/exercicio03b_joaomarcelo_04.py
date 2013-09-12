num = int(input ("num? "))

i = 1
multiplos = []
while(i <= num):
    if num % i ==0:
        multiplos.append(i)
    i+= 1

print(multiplos)
