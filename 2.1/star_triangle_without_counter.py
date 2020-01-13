# Вывод звездочек без счетчика

stars = '*'
n = int(input("Введите количество строк "))
while len(stars)<=n:
    print(stars)
    stars+="*"
