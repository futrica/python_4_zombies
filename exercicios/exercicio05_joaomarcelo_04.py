x = 18644
cont = 0
while x <= 33087:
    if "2" in str(x) and "7" not in str(x):
        cont +=1
    x +=1
print(cont)
