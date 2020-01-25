s = 'AgttCDcc'
p ='cc'

print(s.upper()) #верхний регистр
print(s.lower()) #нижний регистр
print(s.count(p)) #сколько раз p встречается в s
print(s.find(p)) #индекс первого вхождения p в s
print(s.find("Z")) #строка Z не входит в строку s
print(s.replace("c","CC")) #заменяем все вхождения c на CC
print("==============================")

"""Последовательные вызовы методов"""
s = "GGAaTggfsgGFDr"
print(s.upper().count("gg".upper()))