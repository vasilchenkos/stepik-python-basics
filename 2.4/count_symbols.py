s = input()
counter_len = len(s)
counter_symbols = (s.upper().count("g".upper()) + s.upper().count("c".upper()))
result = counter_symbols/counter_len * 100
print(result)