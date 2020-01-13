# вывести нечетные числа

a = int(input("Введите число "))
while a <= 55:
    if a % 2 != 0:
        print(a)
    a+=1