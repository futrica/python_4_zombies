hora = float(input ("quanto ganha por hr? "))
htrab = float(input ("horas trabalhadas? "))

salB = hora * htrab
ir = salB * 11/100
inss = salB * 8/100
sind = salB * 5/100
desc = ir + inss + sind
salL = salB - desc

print("Salario bruto: R$ %0.2f " %salB)
print("IR: R$ %0.2f" %ir)
print("Inss: R$ %0.2f" %inss)
print("Sindicato: R$ %0.2f" %sind)
print("sobrou: R$ %0.2f" %salL)
