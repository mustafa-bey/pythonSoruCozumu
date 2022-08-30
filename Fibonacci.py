#fibonacci sayı dizisinin ilk 10
#elemanın ekrana yazan program

list=[1,2]

for i in range(8):
    list.append(list[i]+list[i+1])

print(list)