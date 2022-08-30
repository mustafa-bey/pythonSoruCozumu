#Girilen 3 basamaklı bir sayının basamaklarının
#küpleri toplamı sayının kendine
#eşit olup olmadığını bulan program

a= abs(int(input("enter a number")))

digit1=a%10

a=(a-digit1)/10

digit2=a%10

digit3=(a-digit2)/10

print("answer = ",digit3**3+digit2**3+digit1**3)
