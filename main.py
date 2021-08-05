def add_all(n):
    if n == 0:
        return 0
    else:
        return n + add_all(n - 1)


def add_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + add_even(n - 1)
    else:
        return 0 + add_even(n - 1)


def add_odd(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return n + add_odd(n - 1)
    else:
        return 0 + add_odd(n - 1)


def your_function(*args, **kwargs):
    s = 0
    for i in args:
        if isinstance(i, (int, float)):
            s += i
    for i in kwargs:
        if isinstance(i, (int, float)):
            s += i
    return s


def is_integer():
    value = input("Input is:\n")
    try:
        int(value)
        return value
    except ValueError:
        return 0


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))
print(add_all(10))
print(add_even(10))
print(add_odd(10))
print(is_integer())
