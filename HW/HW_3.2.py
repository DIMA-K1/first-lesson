# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]


nums = [12, 3, 4, 10, 8]
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()

print(nums)