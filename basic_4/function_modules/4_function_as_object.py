
def multiply(num1, num2):
    return num1 * num2


def add(func, x, y):
    mult = func(x, y)
    final = x + y + mult
    print(final)


operation = multiply
print(operation(2,3))
add(multiply, 2, 3)