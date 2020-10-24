
def sayHai(name):
    print(f"Hai {name}")


def sayHai(name=""):
    print(f"Hai {name}")


def returnDouble(num):
    double = num * num
    return double


sayHai("fajar")
sayHai()
print(returnDouble(5))