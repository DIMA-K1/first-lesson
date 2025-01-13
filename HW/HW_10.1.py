

def some_gen(begin, end, func):
    """
    Генераторная функция для числовой последовательности

    begin: первый элемент последовательности
    end: количество элементов в последовательности
    func: функция, формирующая значение для последовательности
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)

# Пример функции
def pow(x):
    return x ** 2

# Test
from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
