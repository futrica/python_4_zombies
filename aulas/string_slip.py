data = input ("informe uma data: ")

data = data.split("/")

if data[1] == "01":
    print("Jan")
elif data[1] == "02":
    print("Fev")
elif data[1] == "03":
    print("Mar")
elif data[1] == "0":
    print("Abr")
elif data[1] == "05":
    print("Mai")
elif data[1] == "06":
    print("Jun")
elif data[1] == "07":
    print("Jul")
elif data[1] == "08":
    print("Ago")
elif data[1] == "09":
    print("Set")
elif data[1] == "10":
    print("Out")
elif data[1] == "11":
    print("Nov")
else: 
    print("Dez")
