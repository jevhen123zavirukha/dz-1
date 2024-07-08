class Menu:
    def __init__(self):
        self.__categories = []

    def add_category(self, category):
        self.__categories.append(category)

    def __str__(self):
        return "\n".join(map(str, self.__categories))
