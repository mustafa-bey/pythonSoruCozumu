#1-100 arasında kaç asal sayı
#vardır gösteren program

alt = int(input("down: "))
ust = int(input("up: "))

for number in range(alt, ust + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)