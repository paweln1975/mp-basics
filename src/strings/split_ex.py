test_str = "The white dog jumped over a lazy cat"
output = test_str.split()
print(output)

numbers = "484,33,4,5,677"
print(numbers.split(sep=","))

generated_list = [
    '9', ' ',
    '1', '2', ' '
    '4', '5', '6', ' '
    's', ' '
]

values = "".join(generated_list).split()
print(values)

# convert a list of string into int

output_list = []
for n in values:
    if n.isdigit():
        output_list.append(int(n))
print(output_list)

# faster list comprehension
output_com = [int(x) if x.isdigit() else "" for x in values]
print(output_list)

# using map
try:
    output_map = list(map(int, values))
except ValueError:
    print("Value error")
else:
    print(output_map)

