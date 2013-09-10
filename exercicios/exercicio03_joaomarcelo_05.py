a = int(input ("entre um numero inteiro: "))
b = int(input ("entre outro numero inteiro: "))

if (b > a):
    dividendo = b
    divisor = a
else:
    dividendo = a
    divisor = b

while (dividendo % divisor != 0):
    c = dividendo % divisor
    dividendo = divisor
    divisor = c

print("MMC: ", divisor)
