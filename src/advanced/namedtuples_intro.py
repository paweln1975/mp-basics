import collections
Book = collections.namedtuple("Book", ["author", "title", "isbn"])
print(Book)

b = Book(author="John", title="A big step", isbn="848848474744")
print(b)
nb = b._replace(title="A huge step")
print(nb)
