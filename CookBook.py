class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.ingredient_count = 0

    def add_ingredient(self, ingredient_name, quantity, measure):
        ingredient = {
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
        }
        self.ingredients.append(ingredient)
        self.ingredient_count = len(self.ingredients)

class CookBook:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish):
        self.dishes[dish.name] = dish

    def get_dish(self, name):
        return self.dishes.get(name)

    def has_dish(self, name):
        return name in self.dishes

    def save_to_file(self, filename='recipes.txt'):
        with open(filename, 'w', encoding='utf-8') as file:
            for dish_name, dish in self.dishes.items():
                file.write(f"{dish_name}\n")
                file.write(f"{dish.ingredient_count}\n")
                for ingredient in dish.ingredients:
                    file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")
                file.write("\n")

    def to_dict(self):
        result = {}
        for dish_name, dish in self.dishes.items():
            result[dish_name] = dish.ingredients
        return result

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}

        for dish_name in dishes:
            dish = self.get_dish(dish_name)
            if dish:
                for ingredient in dish.ingredients:
                    name = ingredient['ingredient_name']
                    quantity = ingredient['quantity'] * person_count
                    measure = ingredient['measure']

                    if name in shop_list:
                        shop_list[name]['quantity'] += quantity
                    else:
                        shop_list[name] = {
                            'measure': measure,
                            'quantity': quantity
                        }

        return shop_list

def read_cookbook_from_file(filename):
    cook_book = CookBook()

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

        print(content)






# Создаем книгу
cook_book = CookBook()

# Рецепт омлета
omelet = Dish("Омлет")
omelet.add_ingredient('Яйцо', 2, 'шт.')
omelet.add_ingredient('Молоко', 100, 'мл')
omelet.add_ingredient('Помидор', 2, 'шт')
cook_book.add_dish(omelet)

# Рецепт утки
duck = Dish("Утка по-пекински")
duck.add_ingredient('Утка', 1, 'шт')
duck.add_ingredient('Вода', 2, 'л')
duck.add_ingredient('Мед', 3, 'ст.л')
duck.add_ingredient('Соевый соус', 60, 'мл')
cook_book.add_dish(duck)

# Рецепт картофеля
potato = Dish("Запеченный картофель")
potato.add_ingredient('Картофель', 1, 'кг')
potato.add_ingredient('Чеснок', 3, 'зубч')
potato.add_ingredient('Сыр гауда', 100, 'г')
cook_book.add_dish(potato)

cook_book.save_to_file()

# read_cookbook_from_file('recipes.txt')

# cook_book_dict = cook_book.to_dict()
# print("cook_book =", cook_book_dict)





# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }