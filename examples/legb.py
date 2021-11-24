x = 100
VERSION = "3.2.0"


def func(a):
    b = 'bb'
    # Shadowing names (built-in & from outer scope) -- not recommended
    # sum = 0
    # x = 100000000

    # global x
    # x = 1000000

    def inner(c):
        d = 'ddd'
        # Shadowing names (built-in & from outer scope) -- not recommended
        # sum = 0
        # x = 100000000
        # a = 500

        # nonlocal b
        # b = 10000000

        print('Function inner (local) level')
        print('Built-in names:', sum, list, print, int, min, Exception)
        print('Global names:', x, VERSION, func, MyClass)
        print('Enclosing names:', a, b, inner)
        print('Local names:', c, d)

    inner('ccc')

    print('Function func (enclosing) level')
    print('Built-in names:', sum, list, print, int, min, Exception)
    print('Global names:', x, VERSION, func, MyClass)
    print('Local names:', a, b, inner)


class MyClass:
    pass


if __name__ == '__main__':
    func("aa")

    print('Module (global) level')
    print('Built-in names:', sum, list, print, int, min, Exception)
    print('Global names:', x, VERSION, func, MyClass)

    # Shadowing built-in name -- not recommended
    # sum = 0
