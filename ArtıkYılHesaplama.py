#.Verilen yılın artık yıl olup olmadığını bulan program

year=int(input("enter a year "))

if year%4==0:
    print("not a leap year")
else:
    print("leap year")