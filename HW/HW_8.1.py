

def add_one(some_list):
    carry = 1
    for i in range(len(some_list) - 1, -1, -1):
        some_list[i] += carry
        if some_list[i] == 10:
            some_list[i] = 0
            carry = 1
        else:
            carry = 0
            break

    if carry == 1:
        some_list.insert(0, 1)

    return some_list

# Test

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
