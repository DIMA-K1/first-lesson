


def is_even(digit):
    """
    Проверка, является ли число четным
    """
    return digit % 2 == 0

# Test

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
