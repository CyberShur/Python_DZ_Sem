'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

N = int(input('Введите число N: '))

def line(a):
    rez = []
    for i in range(1, a+1):
        if i in [1]:
            rez.append(i)
        else:
            rez.append(rez[-1]*i)
    return rez

res = line(N)

print(res)