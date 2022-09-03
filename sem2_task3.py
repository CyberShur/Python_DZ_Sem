'''
Реализуйте алгоритм перемешивания списка.
'''
import random
numbers = [random.randint(0,10) for i in range(random.randint(3,8))]
print(f"Список: {numbers}")
random.shuffle(numbers)
print(f"Перемешанный список: {numbers}")
