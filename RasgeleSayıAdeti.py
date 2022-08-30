#Rastgele girilen 50 sayıdan negatif olanların
#ve pozitif olanların sayısını bulan program


list=[]

for i in range(5):
    number=int(input("enter a number "))
    list.append(i)

counter=0
counter1=0
counter2=0

for i in list:
    if list[i]<0:
        counter1=counter1+1
    elif list[i]>0:
        counter2=counter2+1
    else:
        counter=counter+1

print("negative = ",counter1)
print("pozitive = ",counter2)
