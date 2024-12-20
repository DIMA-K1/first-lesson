
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
#
# [1, 3, 5] => 30
# [6] => 36
# [] => 0



numbers = [1, 3, 5]
if len(numbers) > 0:
    numbers_sum = 0


    for i in range(len(numbers)):
        if i % 2 == 0:
            numbers_sum += numbers[i]


    result = numbers_sum * numbers[-1]

    print(result)

else:
    print('List empty!')