def get_longer_strings(*strings, n=0):
    result = []
    for string in strings:
        if len(string) > n:
            result.append(string)
    return result


# print('__name__ =', __name__)
if __name__ == '__main__':
    print(get_longer_strings("ana", "banana"))
    print(get_longer_strings("ana", "banana", n=4))
