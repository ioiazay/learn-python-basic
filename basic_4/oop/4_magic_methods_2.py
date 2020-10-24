# __truediv__


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "#" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("Spam")
hello = SpecialString("Hello World")

print(spam / hello)
