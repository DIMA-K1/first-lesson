# 999 -> 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1




number = 1
print(number)

while number > 9:
    temp_number = str(number)
    number = 1
    for char in temp_number:
        if char.isdigit():
            number *= int(char)
    print(number)