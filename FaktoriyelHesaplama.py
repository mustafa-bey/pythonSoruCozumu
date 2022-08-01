#Girilen sayının faktöriyelini bulan program

#lütfen bir x değeri giriniz
x=int(input("please enter an x value "))

fak=1
for i in range(x):
    fak=(i+1)*fak

print("answer =",fak)




