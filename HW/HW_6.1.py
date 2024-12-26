# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA





import string


user_input = "a-c"
letters = string.ascii_letters
parts = user_input.split('-')
start = parts[0]
end = parts[1]
start_index = letters.index(start)
end_index = letters.index(end)

result = letters[start_index:end_index + 1]

print(result)
