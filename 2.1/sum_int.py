# Программа вычисляет сумму числел на отрезке от a до b 

a = int(input("Введите начальное значение отрезка: "))
b = int (input("Введите конечное значение отрезка: "))
s = 0
i = a
while i <= b:
	s+=i
	i+=1
print(s)