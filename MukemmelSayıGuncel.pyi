#girilen sayının mükemmel sayı olup
#olmagığını ekrana yazdıran program

number=int(input("enter a number "))

list=[]

for i in range(1,number+1):
    if number%i==0:
        list.append(i)

sum=0
for i in list:
    sum=sum+i

if number*2==sum:
    print("entered number is perfect number")
else:
    print("entered number is not perfect number")