#.Dışarıdan iki kenarı ve aradaki açısı
#girilen üçgenin alanını hesaplayan program

import math

edge1=int(input("enter a edge "))
edge2=int(input("enter a edge "))
pain=int(input("enter a pain "))

x=(1/2)*edge2*edge1*(math.sin(pain))

print("answer =",x)
