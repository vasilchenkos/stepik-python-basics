s = input()
i = 0
count_str = len(s) - 1
is_palindrom = True
while i < count_str:
    if s[i] != s[count_str]:
        is_palindrom = False
    i += 1
    count_str -= 1
if is_palindrom:
    print("YES")
else:
    print('NO')