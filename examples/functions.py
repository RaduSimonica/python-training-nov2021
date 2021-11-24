# # Required parameters
# def get_diff(a, b):
#     return a - b
#
#
# # Positional arguments
# diff = get_diff(10, 3)
# print(diff)
# # Keyword arguments
# diff = get_diff(b=10, a=3)
# print(diff)


# # Optional parameters
# def get_diff_2(a=0, b=0):
#     return a - b
#
#
# diff = get_diff_2()
# print(diff)
# # Positional arguments
# diff = get_diff_2(10)
# print(diff)
# diff = get_diff_2(10, 3)
# print(diff)
# # Keyword arguments
# diff = get_diff_2(b=10)
# print(diff)
# diff = get_diff_2(b=10, a=3)
# print(diff)


# Variable-length arguments
def arbitrary_arguments(*args, **kwargs):
    print()
    print('args:', args, type(args), len(args))
    print('kwargs:', kwargs, type(kwargs), len(kwargs))


# arbitrary_arguments()
# arbitrary_arguments(10)
# arbitrary_arguments(10, 3)
# arbitrary_arguments(10, 3, 1, 4, 61, 6)
# arbitrary_arguments(arg1=100, arg2=200)
# arbitrary_arguments(1, 2, 3, arg1=100, arg2=200)


words = ['hello', 'hi', 'bye']
arbitrary_arguments(*words)

d = {'apples': 4, 'bananas': 5}
arbitrary_arguments(**d)

d = dict(apples=4, bananas=5, pears=10, oranges=2)
