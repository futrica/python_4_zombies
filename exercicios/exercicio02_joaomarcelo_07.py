area = float(input ("informe m²: "))

tinta  = area / 3
galao = tinta / 18

if (galao % 18 != 0 ):
    galao = int(galao)+1
total = galao * 80

print("vão precisar de %.0f galões e valor a pagar R$ %.2f " %(galao, total))
