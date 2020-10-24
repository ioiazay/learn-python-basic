class Makhluk_Hidup:
    def growth(self):
        print("Im Growth")


class Animal(Makhluk_Hidup):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def happy(self):
        print("yuhuuu")


class Cat(Animal):
    def happy(self):
        print("Meaw")
        super().happy()


class Dog(Animal):
    def happy(self):
        print("Guk Guk")


black_cat = Cat("Black", "Rede")
blue_dog = Dog("Blue", "made")

black_cat.happy()
blue_dog.happy()
blue_dog.growth()