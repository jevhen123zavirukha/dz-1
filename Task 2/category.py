class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish):
        self.__dishes.append(dish)

    def __str__(self):
        dishes = "\n".join(map(str, self.__dishes))
        return f"{self.name}\n{dishes}"
