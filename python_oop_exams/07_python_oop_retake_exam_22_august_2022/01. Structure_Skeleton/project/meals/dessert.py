from project.meals.meal import Meal


class Dessert(Meal):
    TYPE = "Dessert"

    def __init__(self, name: str, price: float, quantity: int = 30):
        super().__init__(name, price, quantity)

    @property
    def meal_type(self):
        return Dessert.TYPE
