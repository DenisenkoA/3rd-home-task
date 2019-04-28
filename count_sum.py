x=input("Введи большое число\n")
total=0
for i in x:
    if int(i)%2!=0:
        total+=pow(int(i),2)
    
print("Результат:",total)
