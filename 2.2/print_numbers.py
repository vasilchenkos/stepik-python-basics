"""Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке."""

i = 0
while i < 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    else:
        print(a)
