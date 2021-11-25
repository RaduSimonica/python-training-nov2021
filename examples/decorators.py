import functools
import time


def make_pretty(func):
    def inner(*args, **kwargs):
        print("I got decorated")
        return func(*args, **kwargs)  # ordinary()
    return inner


def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        time_before = time.time()
        result = func(*args, **kwargs)
        time_after = time.time()
        elapsed = time_after - time_before
        print(f'Elapsed: {elapsed}')
        return result
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@timer
@make_pretty
def greet(name):
    print(f'Hello, {name}!')


@timer
@make_pretty
def increment(nr, step=1):
    return nr + step


@timer
def intense_computing():
    """Assume it does some time-consuming operations"""
    time.sleep(2)


# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner
ordinary()   # make_pretty.<locals>.inner()

greet('Anna')

print(increment(10, 2))

intense_computing()

print(intense_computing.__doc__)
print(intense_computing.__name__)
