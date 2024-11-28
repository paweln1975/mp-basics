from content import recipes, ingredients

display_menu = {}
shopping_list = {}


def add_to_shopping_list(shopping_dict: dict, shop_item: str, amount: int):
    if shop_item in shopping_dict.keys():
        shopping_dict[shop_item] += amount
    else:
        shopping_dict[shop_item] = amount


def create_shopping_list(sel_item: str):
    meal_ingredients = recipes[sel_item]
    for item, amount_req in meal_ingredients.items():
        if item in ingredients:
            amount_avail = ingredients[item]
            print("We have {} of {}".format(amount_avail, item))
            if amount_req > amount_avail:
                add_to_shopping_list(shopping_list, item, amount_req-amount_avail)
                ingredients[item] = 0
            else:
                ingredients[item] = amount_avail - amount_req
        else:
            add_to_shopping_list(shopping_list, item, amount_req)


for index, key in enumerate(recipes):
    display_menu[str(index+1)] = key

for key, value in display_menu.items():
    print("{} - {}".format(key, value))

for i in range(1, 4):
    selected_value = str(i)
    selected_item = display_menu[selected_value]
    print("Create shopping list for:{}".format(selected_item))
    create_shopping_list(selected_item)

# print a shopping list of missing items
for key, value in shopping_list.items():
    print("Shopping item: {} amount needed: {}".format(key, value))


# print ingredients left
for key, value in ingredients.items():
    print("Ingredient left: {} amount: {}".format(key, value))