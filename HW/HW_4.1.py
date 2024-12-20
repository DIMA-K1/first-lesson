# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

nums = [0, 1, 0, 12, 3]

new_list = []

for number in nums:
    if number != 0:
        new_list.append(number)

print(new_list)

zeros_counter = nums.count(0)
print(zeros_counter)

for i in range(zeros_counter):
    new_list.append(0)

print(new_list)