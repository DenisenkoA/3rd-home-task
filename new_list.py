L=[2,4,9,16,25]

#1 for
for i in range(len(L)):
    L[i]=pow(L[i],0.5)
print (L)

#2 map 
L=[2,4,9,16,25]
print("Используя map:\n")
print(list(map((lambda x: x**0.5),L)))

#3 generator
L=[2,4,9,16,25]
print("Используя генератор:\n")
for i in range(len(L)):
    L[i]=L[i]**0.5
print (L)
