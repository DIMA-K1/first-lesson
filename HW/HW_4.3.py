
import random

numbers = []

for i in range(random.randint(3, 10)):
    numbers.append(random.randint(3, 10))

print(numbers)
result_list = [numbers[0], numbers[2], numbers[-2]]
print(result_list)