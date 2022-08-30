#Girilen decimal (onluk) bir sayının binary
#(ikilik) bir sayıya dönüştüren program

number=int(input("enter a number "))
list=[]
i=0
while i<10:
    i=i+1
    a=number/2
    ans=int(a)

    tmp=number-ans*2
    list.append(tmp)
    number=ans

print(list[::-1])