"""Вывести сумму всех нечетных чисел на промежутке от a до b"""

a = int(input())
b = int(input())
s = 0
if a % 2 == 0:
    a+=1
for i in range(a,b+1,2):
    s+=i
print(s)