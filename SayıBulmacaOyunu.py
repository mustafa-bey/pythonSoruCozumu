#sayı tahmin oyunu

import random

guess=random.randint(1,10)
print(guess)

i=0
while i<10:
    i=i+1
    a=int(input("guess ? "))

    if guess==a:
        print("congratulations find number")
        break
    elif a>guess:
        print("down")
    else:
        print("up")

print("game over")