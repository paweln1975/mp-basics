from content import recipies, ingredients

display_menu = {}

for index, key in enumerate(recipies):
    print(index, key)
    display_menu[str(index+1)] = key

for key, value in display_menu.items():
    print("{} - {}".format(key, value))

selected_value = "1"
selected_item = display_menu[selected_value]
print(selected_item)

meal_ingredients = recipies[selected_item]
print(meal_ingredients)

for item, amount_req in meal_ingredients.items():
    if item in ingredients:
        amount_avail = ingredients[item]
        print("We have {} of {}".format(amount_avail, item))
        if amount_req > amount_avail:
            print("WARN for {} - not enough.".format(item))
    else:
        print("No ingredient: {}".format(item))

# create a shopping list of missing items



