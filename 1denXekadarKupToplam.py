#1'den x'e kadar olan sayılarının
#küplerinin toplamını bulan program

first=1
sum=0
cube=0
i=1

#lütfen bir x değeri giriniz
x=int(input("please enter an x value "))

for first in range(x):
    sum = (i*i*i)
    i=i+1
    cube=sum+cube

print("cube of numbers =",cube)