import random 
print("Компьютер загадал число от 0 до 10 \n У вас есть три попытки. Удачи!")
y=random.randint(0,11)

attempts=3

while attempts>0:
    attempts=attempts-1
    x=int(input("Угадайте число или напишите ""стоп"" чтобы закончить игру:\n"))
    if x=="стоп":
        print("Вы закончили игру")
        break
    elif x==y:
        print('Победа!')
        break
    elif x>=y:
        print("Вы проиграли,ваше число было больше")
    else:
        print("Вы проиграли,ваше число было меньше")
        
if attempts==0:
    print("Game over :(") 
