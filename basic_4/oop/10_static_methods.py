class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No Pineapples!")
        else:
            return True


bahan = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in bahan):
    pizza = Pizza(bahan)