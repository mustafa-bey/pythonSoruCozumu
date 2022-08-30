#klavyeden girilen 25 adet sayıdan
#negatiflerin toplamı,çift sayıların çarpımını
#ve 7 rakamına eşit olanların sayısını yazdıran program

list1=[]

for i in range(5):
    number=int(input("enter a number "))
    list1.append(number)

counter=0
negative=0
pozitive=1

for i in list1:
    if i==7:
        counter=counter+1
    elif i<0:
        negative=negative+i
    elif i>0:
        pozitive=pozitive*i

print("7 number = ",counter)
print("sum of negative = ",negative)
print("products of pozitive = ",pozitive)