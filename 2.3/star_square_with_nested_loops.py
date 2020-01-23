"""Вывести квадрат из звезд с помощью вложенных циклов"""
n = int(input())

for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
