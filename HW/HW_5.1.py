# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True



import string
import keyword


test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']

for test_variable in test_data:
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:
            print(f"Error! Found {test_variable} is keyword!")
        elif test_variable.find('__') != -1:
            is_correct = False
            print(f'Error! Found double "_" in {test_variable} variable name!')
        elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.find(' ') == -1:
            is_correct = True
            for symbol in string.punctuation.replace('_', ''):
                if symbol in test_variable:
                    is_correct = False
                    print(f'Error! Found {test_variable} in variable name!')
                    break

            if is_correct:
                print(f'Keyword {test_variable} is correct!')
        else:
            print(f'Error! Found {test_variable} in variable name!')
    else:
        print('Incorrect variable length!')