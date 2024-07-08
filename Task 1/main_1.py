# Task 1
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asc time)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class PriceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Dish:

    def __init__(self, name: str, price: int | float):

        if not isinstance(price, int | float):
            logger.error(" Price must be an integer or float")
            raise TypeError(" Price must be an integer or float")
        if price <= 0:
            logger.error(" Price must be greater than 0")
            raise PriceError(" Price must be greater than 0")

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} UAH"


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        dishes = "\n".join(map(str, self.__dishes))
        return f"{self.name}\n{dishes}"


class Menu:
    def __init__(self):
        self.__categories = []

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return "\n".join(map(str, self.__categories))


if __name__ == "__main__":
    try:
        dish_1 = Dish("Pizza", 10)
        dish_2 = Dish("Pasta", 20)
        dish_3 = Dish("Salad", 20)
        dish_4 = Dish("Soup", 4)
        dish_5 = Dish("Steak", 20)
        dish_6 = Dish("Burger", 7)

        category_1 = Category("Main Course")
        category_1.add_dish(dish_1)
        category_1.add_dish(dish_2)
        category_1.add_dish(dish_3)

        category_2 = Category("Appetizer")
        category_2.add_dish(dish_4)
        category_2.add_dish(dish_5)
        category_2.add_dish(dish_6)

        menu = Menu()
        menu.add_category(category_1)
        menu.add_category(category_2)

        print(menu)

    except ValueError as a:
        print(a)
