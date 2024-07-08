# Task 2
from dish import Dish
from category import Category
from menu import Menu


if __name__ == "__main__":
    try:
        dish_1 = Dish("Pizza", 10)
        dish_2 = Dish("Pasta", 14)
        dish_3 = Dish("Salad", 20)
        dish_4 = Dish("Soup", 120)
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
