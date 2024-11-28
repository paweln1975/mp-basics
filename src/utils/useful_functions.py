from functools import reduce

print("=" * 80)
print("Python's reduce() function iterates over each item in a list, or any other iterable data type, " +
      "and returns a single value.")


def add_num(a, b):
    return a+b


a = [1, 2, 3, 10]
print(reduce(add_num, a))

print("=" * 80)
print("The split() function breaks a string based on set criteria.")
words = "column1 column2 column3"
words = words.split(" ")
print(words)

print("=" * 80)
print("The enumerate() function returns the length of an iterable and loops through its items simultaneously.")
fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits, start=1):
    print(i, j)

print("=" * 80)
print("Python's eval() function lets you perform mathematical operations on integers or floats, " +
      "even in their string forms.")
g = "(4 * 5)/4"
d = eval(g)
print(d)

print("=" * 80)
print("You can round up the result of a mathematical operation to a specific number of significant " +
      "figures using round():")
raw_average = (4+5+7/3)
rounded_average = round(raw_average, 2)
print("The raw average is:", raw_average)
print("The rounded average is:", rounded_average)


print("=" * 80)
print("The max() function returns the highest ranked item in an iterable. Min() does the opposite.")
b = {1:"grape", 2:"apple", 3:"applesss", 4:"zebra", 5:"mango"}
print(max(b.values()))
print(min(b.values()))

print("=" * 80)
print("TLike reduce(), the map() function lets you iterate over each item in an iterable. However, instead of " +
      "producing a single result, map() operates on each item independently.")
tab_b = [1, 3, 4, 6]
tab_a = [1, 65, 7, 9]

c = map(add_num, tab_b, tab_a)
for i, item in enumerate(c):
    print(item)

print("=" * 80)
print("Python's getattr() returns the attribute of an object. It accepts two parameters: the class and the" +
      " target attribute name.")


class ty:
    def __init__(self, number, name):
        self.number = number
        self.name = name


obj_a = ty(5 * 8, "Idowu")
name = getattr(obj_a, 'name')
print(name)

print("=" * 80)
print("append(): It works by writing new data into a list without overwriting its original content.")
nums = [1, 2, 3]
appendedlist = [2, 4]
for i in nums:
    a = i*3
    appendedlist.append(a)
print(appendedlist)

print("=" * 80)
print("range(): It's handy if you want to create a list of integers ranging between specific numbers without " +
      "explicitly writing them out.")
a = range(1, 6)
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)

print("=" * 80)
print("Although the slice() function and the traditional slice method give similar outputs, using slice() " +
      "in your code can make it more readable.")
b = [1, 3, 4, 6, 7, 10]
st = "Python tutorial"
sliceportion = slice(0, 4)
print(b[sliceportion])
print(st[sliceportion])

print("=" * 80)
print("Python's strip() removes leading characters from a string. It repeatedly removes the first character from " +
      "the string, if it matches any of the supplied characters.")
st = " Python tutorial"
st = st.strip(" P")
print(st)

print("=" * 80)
print("The sorted() function works by making a list from an iterable and then arranging its values in descending" +
      " or ascending order")
f = {1, 4, 9, 3} # Try it on a set
sort = {"G":8, "A":5, "B":9, "F":3} # Try it on a dictionary
print(sorted(f, reverse=True))   # Descending
print(sorted(sort.values()))     # Ascending (default)

print("=" * 80)
print("The join() function lets you merge string items in a list.")
a = ["Python", "tutorial", "on", "MUO"]
a = " ".join(a)
print(a)

print("=" * 80)
print("Python's replace() method lets you replace some parts of a string with another character")
columns = ["Cart_name", "First_name", "Last_name"]
for i in columns:
    i = i.replace("_", " ")
    print(i)
