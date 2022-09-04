'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, -2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


number = int(input("Введите число: "))

def fibo(n):
    f1 = 1
    f2 = 1
    if n == 0:
        fib = [0]
        return print(fib)
    elif n==1:
        fib = [-1, 0, 1]
        return print(fib)
    else:
        fib = [1, 1]
        while n > 2:
            f1, f2 = f2, f1 + f2
            n = n - 1
            fib.append(f2)
        fib2 = list(fib)
        fib2.reverse()
        for i in range(len(fib2)):
            if fib2[i] > 0:
                fib2[i] = fib2[i]*(-1)
        fib.insert(0, 0)
        return print(fib2 + fib)
        
fibo(number)



