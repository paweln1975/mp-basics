import random as r
import datetime
from functools import reduce

print("=" * 80)
print("Convert String to Integer")
str1 = '100'
print(int(str1))

print("=" * 80)
print("Reverse a List")
arr = [1, 2, 3, 4, 5, 6]
print(arr)

reversedArr = arr[::-1]
print(reversedArr)

reversedArr = list(reversed(arr))
print(reversedArr)

arr.reverse()
print(arr)

print("=" * 80)
print("Swap Two Variables")
a = 3
b = 5

b, a = a, b
print(f"a={a}, b={b}")

print("=" * 80)
print("FizzBuzz")

[print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i, end=" ") for i in range(1, 31)]
print()

print("=" * 80)
print("Generate Random Password")
p = 'abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)'
print(''.join([p[r.randint(0, len(p) - 1)] for i in range(10)]))

print("=" * 80)
print("Display the Current Date and Time in String Format")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("=" * 80)
print("Check if a String Is a Palindrome")
str1 = "madam"
str2 = "MAKEUSEOF"
print('Yes') if str1 == str1[::-1] else print('No')
print('Yes') if str2 == str2[::-1] else print('No')

print("=" * 80)
print("Find Factorial of a Number")
num1 = 10
factorial = lambda num: 1 if num <= 1 else num * factorial(num - 1)
print("Factorial of", num1, ":", factorial(num1))

print("=" * 80)
print("Print Fibonacci Sequence Upto N Terms")
fibSequence = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fibSequence(10))

print("=" * 80)
print("Calculate the Sum of a List")
list1 = [1, 2, 3, 4, 5, 6, 7]
print(sum(list1))

print("=" * 80)
print("Sort a List")
list1 = [12, 345, 123, 34, 23, 37]
print(sorted(list1))
list1.sort()
print(list1)
