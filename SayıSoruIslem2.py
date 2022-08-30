#1ile 500 arasındaki tam sayılardan tek sayıların
#toplamı ile çift sayıların toplamının farkı
#negatif mi, pozitif mi olduğunu bulan program

sum1=0
sum2=0

for i in range(500):
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i

print("answer = ",sum2-sum1)