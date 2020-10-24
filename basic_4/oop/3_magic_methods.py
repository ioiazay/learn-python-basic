# __add__


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)


first = Vector2D(1, 2)
seconds = Vector2D(4,5)

add_result = first + seconds
sub_result = first - seconds
mul_result = first * seconds

print(f"{add_result.x}:{add_result.y}")
print(f"{sub_result.x}:{sub_result.y}")
print(f"{mul_result.x}:{mul_result.y}")
