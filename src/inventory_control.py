def check_ingredients(ingredients, current):
    all_ingredients = True

    for ingredient in ingredients:
        if current[ingredient] > 0:
            current[ingredient] -= 1
        else:
            all_ingredients = False

    return all_ingredients


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.__used_ingredients = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        ingredients = self.INGREDIENTS[order]

        for ingredient in ingredients:
            if (
                self.__used_ingredients[ingredient]
                < self.MINIMUM_INVENTORY[ingredient]
            ):
                self.__used_ingredients[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.__used_ingredients

    def get_available_dishes(self):
        current = {}

        for item, qnt in self.__used_ingredients.items():
            current[item] = self.MINIMUM_INVENTORY[item] - qnt

        available = []

        for dish, ingredients in self.INGREDIENTS.items():
            have_all = check_ingredients(ingredients, current)
            if have_all:
                available.append(dish)

        return set(available)
