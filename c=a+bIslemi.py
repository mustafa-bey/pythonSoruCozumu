#Girilen a ve b sayısı 50'den büyük
#olduğunda c=a+b işlemini yapan değilse bu
#sayılar uygun değil yazdıran program

a=int(input("enter a number "))
b=int(input("enter a number "))

if a>50 and b>50:
    print("answer = ",a+b)
else:
    print("numbers are not suitable")