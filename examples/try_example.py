s = "hello world"
substring = input("Searched substring: ")

try:
    idx = s.index(substring)
    print('Next letter:', s[idx + 1])
    if idx > 5:
        raise KeyError
except ValueError as ex:
    print('Value not found;', ex)
except IndexError as ex:
    print('Index not found;', ex)
else:
    print('No exception occurred')
finally:
    print('Executes anyways')

print('Outside try-except')
