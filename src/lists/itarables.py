"""
Testing itertools module
>>> import sys; sys.tracebacklimit = 0
>>> import itertools
>>> print_under_budget_meals(main_courses, price_main_courses, desserts, price_desserts, drinks, price_drinks, 30)
fried fish ice-cream cola 28
fried fish cake cola 30

>>> print_under_budget_meals_ver1(main_courses, price_main_courses, desserts, price_desserts, drinks, price_drinks, 40)
beef stew ice-cream cola 33
beef stew ice-cream wine 40
beef stew cake cola 35
fried fish ice-cream cola 28
fried fish ice-cream wine 35
fried fish cake cola 30
fried fish cake wine 37

>>> print_under_budget_meals_ver2(main_courses, price_main_courses, desserts, price_desserts, drinks, price_drinks, 50)
beef stew ice-cream cola 33
beef stew ice-cream wine 40
beef stew cake cola 35
beef stew cake wine 42
fried fish ice-cream cola 28
fried fish ice-cream wine 35
fried fish cake cola 30
fried fish cake wine 37

"""
import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]


def print_under_budget_meals(main_courses, price_main_courses,
                             desserts, price_desserts,
                             drinks, price_drinks, limit):
    main_course_list = list(zip(main_courses, price_main_courses))
    dessert_list = list(zip(desserts, price_desserts))
    drink_list = list(zip(drinks, price_drinks))

    food_list = [(main_course[0], dessert[0], drink[0], main_course[1]+dessert[1]+drink[1])
             for main_course, dessert, drink in itertools.product(main_course_list, dessert_list, drink_list)
             if main_course[1]+dessert[1]+drink[1] <= limit]

    for item in food_list:
        print(*item)

def print_under_budget_meals_ver1(main_courses, price_main_courses,
                             desserts, price_desserts,
                             drinks, price_drinks, limit):
    for food, price in zip(itertools.product(main_courses, desserts, drinks),
                           itertools.product(price_main_courses, price_desserts, price_drinks)):
       if sum(price) <= limit:
            print(*food, sum(price))

def print_under_budget_meals_ver2(main_courses, price_main_courses,
                             desserts, price_desserts,
                             drinks, price_drinks, limit):
    menu = itertools.product(main_courses, desserts, drinks)
    price = (sum(prices) for prices in itertools.product(price_main_courses, price_desserts, price_drinks))

    for m, p in zip(menu, price):
        if p <= limit:
            print(*m, p)