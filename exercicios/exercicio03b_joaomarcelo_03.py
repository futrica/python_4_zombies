num = int(input ("entre com um numero int: "))

div = 1
a = 0
while(div < num):
    if (num %  div == 0):
        a +=1
    div +=1

if a < 2:
    print("o num %d é primo" %num)
else:       
    print("o num %d não é primo" %num)
    
