list_1 = ["A", "B", "C"]
tuple_1 = ("A", "B", "C")

print(*tuple_1)

def add_numbers(*nums):
    """
    * packs the element into a tuple
    """
    print(nums)
    print(type(nums))
    return sum(nums)


def disp_numbers(**nums):
    for key, value in nums.items():
        print(f"Key={key} Value={value}")



print(add_numbers(1, 2, 3, 4, 5))
print(disp_numbers(one=1, two=2, three=3, four=4))

phrase = [('A', 'Away'), ('F', 'From'), ('K', 'Keyboard')]
unzipped = zip(*phrase)
a, b = list(unzipped) # unpacking the list
print(list(unzipped))
print(a)
print(b)

zipped = zip(iter(list_1), iter(tuple_1))
print(list(zipped))

# please do not modify the following code
_d_list = [keyword.split(':') for keyword in 'common name:dog, species:Canis familiaris'.split(', ')]
domestic_animal = {key: value for key, value in _d_list}
_w_list = [keyword.split(':') for keyword in 'common name:wolf, species:Canis lupus'.split(', ')]
wild_animal = {key: value for key, value in _w_list}

# your code here
for a, b in zip(domestic_animal.items(), wild_animal.items()):
    print("The domestic animal's " + a[0] + " is '" + a[1] + "'.")
    print("The wild animal's " + b[0] + " is '" + b[1] + "'.")

# please do not modify the following code
numbers, word = '1234 word'.split()
numbers = list(numbers)

# your code here
list_of_tuples = [(int(num), w) for num, w in zip(numbers, word)]
print(list_of_tuples)


# please do not modify the following code
interest_rates = [float(x) for x in '0.02, 0.05, 0.04'.split(',')]
years = [int(x) for x in '2, 3, 5'.split(',')]
loan_principals = [int(x) for x in '1000, 2000, 1400'.split(',')]

for interest_rate, year, loan_principal in zip(interest_rates, years, loan_principals):
    print(int(interest_rate * year * loan_principal))