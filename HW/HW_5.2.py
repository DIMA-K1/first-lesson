
while True:

    number1 = int(input('Enter the first number:'))
    number2 = int(input('Enter the second number:'))
    user_select = int(input("1. +\n2. -\n3. *\n4. /\nSelect your choice: "))

    match user_select:
        case 1:
            result = number1 + number2
            print(result)
        case 2:
            result = number1 - number2
            print(result)
        case 3:
            result = number1 * number2
            print(result)
        case 4:
            match number1 == 0 or number2 == 0:
                case 1:
                    print('Invalid input please try again')
                case _:
                    result = number1 / number2
                    print(result)
        case _:
            print("Invalid input please try again")

    user_input = input("Enter 'n' to exit the program or enter 'y' key to continue: ")
    if user_input == "n":
        print("Exit from program!")
        break