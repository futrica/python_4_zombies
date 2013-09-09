a = float(input ("entre com a lado A: "))
b = float(input ("entre com a lado B: "))
c = float(input ("entre com a lado C: "))

if (a < b + c) and (b < a +c ) and (c < a + b):
    if (a == b) and (b == c):
        print("equilatero")
    else:
        if (a ==b ) or (a ==c ) or (b ==c ):
            print ("isosceles")
        else:
            print("escaleno")
else:
    print("as medidas passadas não forma triangulo")
