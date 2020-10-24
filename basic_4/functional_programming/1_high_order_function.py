
def add_five(x):
    return x + 5


def multiply(func, num):
    return func(num) ** 2


print(multiply(add_five, 5))