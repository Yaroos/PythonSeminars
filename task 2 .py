# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

input = int(input ('Введите трех значное число: '))
a = input % 10
print(a)
b = int(input / 10) % 10
print(b)
c = int(input / 100) % 10
print(c)
final = a + b + c
print(final)