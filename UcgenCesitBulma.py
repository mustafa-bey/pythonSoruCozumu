#iç açıları verilen üçgenin karar ağacı

print("edge degree should be max 180 degrees")
print("The entered values must satisfy the triangle condition.")

edge1=int(input("enter a degree "))
edge2=int(input("enter a degree "))
edge3=int(input("enter a degree "))

if edge1+edge3+edge2>180:
    print("error")
    breakpoint()

if edge1!=edge2!=edge3:
    print("scalene triangle")
elif edge1==edge3==edge2:
    print("equilateral triangle")
elif edge1==edge2 or edge1==edge3 or edge2==edge3:
    print("isosceles triangle")
