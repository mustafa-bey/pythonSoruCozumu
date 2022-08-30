# ax2+bx+c=0 tipindeki bir denklemin
#köklerini bulan program

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

delta = b ** 2 - 4 * a * c

if (delta < 0):
    print("not a reel root.")
elif (delta == 0):
    print("first root = second root :", (-b / 2 * a))
else:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print("first root : {}\nsecond root : {}".format(x1, x2))