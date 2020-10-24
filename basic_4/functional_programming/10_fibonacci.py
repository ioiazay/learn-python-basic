num = 10


def fibonaci(n):
    x = 0
    y = 1
    nums = [x, y]

    for i in range(n):
        new = x + y
        nums.append(new)
        x = y
        y = new

    for nu in nums:
        print(nu)


fibonaci(num)
