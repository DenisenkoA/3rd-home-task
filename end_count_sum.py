result = 0
while True:
    num = input("Введите число или Стоп для выхода:\n")
    if num == 'Стоп' or num=="стоп":
        break
    else:
        if num.isdigit():
            result += int(num)
        else:
            print("Ошибка ввода.")
        
print("Сумма чисел:", result)
