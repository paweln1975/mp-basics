"""
Walrus operator training
Looks like the eyes and tusks of a walrus on its side
- ponieważ wygląda jak oczy i kły morsa z boku
>>> import sys; sys.tracebacklimit = 0
>>> data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}, {'name': 'David'}]
>>> filtered_data = filter_data_with_walrus(data, 31)
>>> filtered_data
[{'name': 'Charlie', 'age': 35}]

>>> numbers = [10, 20, 30, 40, 50]
>>> threshold = 25
>>> above_threshold, below_threshold = filter_numbers(numbers, threshold)
>>> above_threshold
[30, 40, 50]
>>> below_threshold
[10, 20]
"""

def filter_data_with_walrus(data: list, age_threshold) -> list:
    filtered_data = [item for item in data
                        if (age := item.get('age')) is not None and age >= age_threshold]
    return filtered_data

def filter_numbers(numbers, threshold):
    above_threshold = [n for n in numbers if n >= threshold]
    below_threshold = [n for n in numbers if n < threshold]
    # Your code here

    return above_threshold, below_threshold


even_numbers = []
odd_numbers = []
n1 = ['1', '3', '5', '8', 'done']
i = 0
while (n := n1[i]) != 'done':
    even_numbers.append(int(n)) if int(n) % 2 == 0 else odd_numbers.append(int(n))
    i = i+1

print(f'Even Numbers: {even_numbers}')
print(f'Odd Numbers: {odd_numbers}')