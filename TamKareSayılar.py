#10 ile 1000 arasındaki tam kare
#sayııları yazdıran program

list=[]

for i in range(1000):
    if i**2<1000:
        list.append(i*i)

print(list)