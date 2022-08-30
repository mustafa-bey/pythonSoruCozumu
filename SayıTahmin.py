#1'den 63'e kadar olan sayılar arasında
#istenilen sayıyı maksimum 6 seferde bulan program

desired_number=int(input("enter a number "))

i=0
while i<6:
    i=i+1
    guess=int(input("guess ? "))

    if guess<desired_number:
        print("")


        #BU SORUYA BAK