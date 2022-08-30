#Girilen sayının abundant (güçlü) sayı mı ya da
#Deficient (güçsüz) sayı mı olduğunu bulan program

def faktoriyel(numara):
    fakt = 1
    for i in range(1, numara + 1):
        fakt *= i
    print("Fatoriyel : ", fakt)

number=int(input("enter a number "))

list=[]
while number>10:
    a=number%10
    list.append(a)
    number=(number-a)/10

list.append(number)
print(list)

list2=[]
for i in list:
    faktoriyel(i)
    list2.append(faktoriyel(i))


