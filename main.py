import os
from pprint import pprint

basic_path = os.getcwd()
recipes_file = 'recipes.txt'
full_path = os.path.join(basic_path, recipes_file)
item_keys = ['Ingredient name', 'quantity', 'measure']


def list_recipes(recipes_path):
    with open(recipes_path, encoding='utf-8') as recipe_file:
        cook_book = {}
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
                    cook_item[item_keys[1]] = int(quan)
                    cook_item[item_keys[2]] = mes
                cook_items.append(cook_item)
                cook_book[cook_name] = cook_items
            recipe_file.readline()
        return cook_book


# pprint(list_recipes(full_path), sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = list_recipes(full_path)
    shop_list = {}
    for item in dishes:
        for items in cook_book[item]:
            list_dishes = {}
            list_dishes.update(items)
            ing = list_dishes.pop(item_keys[0])
            list_dishes[item_keys[1]] *= person_count
            if ing in shop_list:
                list_dishes[item_keys[1]] += list_dishes[item_keys[1]]
                shop_list[ing] = list_dishes
            else:
                shop_list[ing] = list_dishes
    return shop_list


shopping_list = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Утка по-пекински'], 3)
pprint(shopping_list, sort_dicts=False)
