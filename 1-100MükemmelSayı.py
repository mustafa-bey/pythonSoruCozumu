#1-100 arasındaki çift sayıların toplamının
#mükemmel sayı olup olmadığını bulan program

sum=0
for i in range(100):
    if i%2==0:
        sum=sum+i

list=[]
for i in range(1,sum+1):
    if sum%i==0:
        list.append(i)

sum2=0
for i in list:
    sum2=sum2+i

if sum*2==sum2:
    print("entered number is perfect number")
else:
    print("entered number is not perfect number")
