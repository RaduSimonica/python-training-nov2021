def input_number(what_number):
    user_integer = None
    while user_integer is None:
        user_input = input(f'Input {what_number} number: ')
        try:
            should_exit(user_input)# pare sa nu aiba logica, dar arunc o exceptie pe care o handleuiesc in main while pentru exit.
            user_integer = int(user_input)
        except ValueError:
            print(f'{x} is not a number! Try again')
        return user_integer


def should_exit(user_input):
    if user_input == 'exit':
        print('See you later! Bye!')
        raise InterruptedError


while True:
    try:
        x = input_number('1st')
        y = input_number('2nd')
    except InterruptedError:
        break

    print(f"First number is: {x}")
    print(f"Second number is: {y}")
    try:
        print(f"First number divided by second number is: {x / y}")
    except ArithmeticError as e:
        print("Oups! Try again with other numbers.", str(e).capitalize())