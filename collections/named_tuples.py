from collections import namedtuple

person_template = namedtuple('Person', ['name', 'age', 'occupation'])

paul = person_template('Paul', 49, 'Manager')
emilia = person_template('Emilia', 15, 'student')
monika = person_template._make(['Monika', 49, 'accountant'])
print(paul)
print(emilia)
print(monika)
monika = monika._replace(age=50)
print(monika)
print(monika._asdict())


print("#########  Training 1  #########")

student_template = namedtuple('Student', ['name', 'age', 'department'])
s1 = student_template('Alina', '22', 'linguistics')
s2 = student_template('Alex', '25', 'programming')
s3 = student_template('Kate', '19', 'art')

print(s1)
print(s2)
print(s3)