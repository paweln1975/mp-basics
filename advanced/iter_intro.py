from advanced.lambda_intro import list1

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 6, 6, 6, 6]

for item1, item2 in zip(list1, list_2):
    print(f"Item={item1}, {item2}")

for index, item2 in enumerate(list_2):
    print(f"Item index={index + 1}, {item2}")


class PowerOfTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n = self.n + 1
            return result
        else:
            raise StopIteration


for value in PowerOfTwo(5):
    print(value, end=', ')

student_list = ["Paul", "Monika", "Emilia", "Ola"]

for index, item in enumerate(student_list):
    print(f"{index+1} {item}")


v1 = (1, 2, 3, 4, 5)
v2 = tuple(reversed(v1))

print(v1)
print(v2)

v3 = (val1 + val2 for val1, val2 in zip(v1, v2))
for v in v3:
    print(v)

str1 = "age"
str2 = "lake"

str3 = (s1 + s2 for s1, s2 in zip(str1, str2))
for s3 in str3:
    print(s3, end='')

english = ["hello", "house"]
spanish = ["ola", "casa"]
french = ["ciao", "maison"]

print()

combined_gen = ((e, s, f) for e, s, f in zip(english, spanish, french))
for t1 in combined_gen:
    e, s, f = t1
    print(f"{e} {s} {f}")

for words in zip(english, spanish, french):
    print(*words)




