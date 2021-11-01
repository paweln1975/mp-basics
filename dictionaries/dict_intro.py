from typing import Dict


def iter_over_dict(dict1):
    for key in dict1:
        print("key: {} value: {}".format(key, dict1[key]))
    for key, value in dict1.items():
        print("key: {} value: {}".format(key, value))


vehicles: Dict[str, str] = {'opel': 'Mokka 1.4', 'vw': 'VW Up!', "plane": "F19", "bike": "Unibike"}

my_car = vehicles['opel']
print(my_car)

your_car = vehicles['vw']
print(your_car)

your_car = vehicles.get("vw")  # if value does not exist it returns None
print(your_car)

vehicles["plane"] = "Jambo Jet"  # changing or adding
del vehicles["bike"]

iter_over_dict(vehicles)

your_car = vehicles.pop("vw", None)
print(your_car, len(vehicles.values()))
