animals = {"Horse", "Dog", "Cat"}
home_animals = {"Dog", "Cat"}

print(f"Home animals are subset of animals: {home_animals.issubset(animals)}")
print(f"Animals are subset of home animals: {animals.issuperset(home_animals)}")
print(f"Set is superset of itself: {animals.issuperset(animals)}")
print(f"Set is subset of itself: {animals.issubset(animals)}")

print("*" * 80)

print(f"Compare 1: {animals > home_animals}")
print(f"Compare 2: {animals >= home_animals}")
print(f"Compare 3: {home_animals < animals}")
print(f"Compare 4: {animals >= animals}")
print(f"Compare 5: {animals == home_animals}")