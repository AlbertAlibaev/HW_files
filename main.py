import os
from pprint import pprint

basic_path = os.getcwd()
recipes_file = 'recipes.txt'
full_path = os.path.join(basic_path, recipes_file)


def list_recipes(recipes_path):
    with open(recipes_path, encoding='utf-8') as recipe_file:
        cook_book = {}
        item_keys = ['Ingredient name', 'quantity', 'measure']
        for line in recipe_file:
            cook_name = line.strip()
            quantity = recipe_file.readline()
            item_list = []
            cook_items = []
            for item in range(int(quantity)):
                item_list.append(recipe_file.readline().strip().split(' | '))
                cook_item = {}
                for ing, quan, mes in item_list:
                    cook_item[item_keys[0]] = ing
                    cook_item[item_keys[1]] = quan
                    cook_item[item_keys[2]] = mes
                cook_items.append(cook_item)
                cook_book[cook_name] = cook_items
            recipe_file.readline()
        return cook_book


pprint(list_recipes(full_path), sort_dicts=False)
