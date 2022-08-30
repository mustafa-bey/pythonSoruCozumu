#girilen 20 adet sayıdan tek sayı ve çift
#sayıların toplamının oranını bulan program

list=[]

for i in range(20):
    a = int(input("enter a number "))
    list.append(a)

single=0
double=0

for i in list:
    if i%2==0 :
        double=double+i
    else:
        single=single+i


print("single numbers = ",single)
print("double numers = ",double)

print("answer = ",double/single)