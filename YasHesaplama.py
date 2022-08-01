#Doğum tarihi girilen kişinin
#yaşını hesaplayan program(basit)

year=int(input("what year are we in"))
birday_year=int(input("what time did you born "))

x=year-birday_year
print(f"you are {x}  years old")



#Doğum tarihi girilen kişinin
#yaşını hesaplayan program(orta)

import datetime as dt
dogum=input("what time did you born: (Gün.Ay.Yıl) ")
dogum=dt.datetime.strptime(dogum,"%d.%m.%Y")
simdi=dt.datetime.now()
fark=simdi-dogum
Yıl=fark.days//365
Ay=fark.days%365//30
Gün=fark.days%365%30
print(f"{Yıl} yıl {Ay} ay {Gün} gündür hayattasınız")


