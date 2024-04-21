from collections import OrderedDict

marks = OrderedDict()
marks['Ann'] = 9.5
marks['Em'] = 8.5
marks['Paul'] = 7.5

my_dict = {'Paul': 7.5, 'Em': 8.5, 'Ann': 9.5}

print(marks)
print(my_dict)
print(OrderedDict(my_dict))

print(marks.popitem(last=True))
print(marks)
marks.update(my_dict)
print(marks)
marks.move_to_end('Em', last=False)
marks.move_to_end('Paul', last=False)
print(marks)
print(marks == OrderedDict(my_dict))


# training
print("#########  Training 1  #########")
marks = {"Tom": 98, "Lina": 92, "Natalie": 81}

marks.update({"Max": 100})
marks = OrderedDict(marks)
marks.move_to_end('Max', last=False)
print(marks)

print("#########  Training 2  #########")
firms = OrderedDict({"YourHouse": 9.5,
                     "BrownBuildCo": 9.1,
                     "Build in the City": 9.0,
                     "mr.Stone & Co": 7.8,
                     "Flinstones Appartment": 7.3})
firms.popitem(last=True)
firms.popitem(last=True)
print(firms)


