'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

x = [2, 3, 5, 9, 3, 5, 3]
length = len(x)
res = 0

for i in range(length):
    if i%2 != 0:
        res = res + x[i]

print(res)