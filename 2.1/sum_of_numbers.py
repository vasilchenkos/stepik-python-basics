# сумма чисел на отрезке

sum = 0
a = int(input("Введите начальное число отрезка "))
b = int(input("Введите конечное число отрезка "))
i = a
while i <= b:
    sum += i
    i += 1
print(sum)