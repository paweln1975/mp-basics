from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import registry


class Employee(object):

    def __init__(self, employee_id, lastname, firstname, title, address, email):
        self.EmployeeId = employee_id
        self.LastName = lastname
        self.FirstName = firstname
        self.Title = title
        self.Address = address
        self.Email = email


engine = create_engine('sqlite:///chinook.db', echo=True)
connection = engine.connect()

metadata = MetaData()
employees = Table('employees', metadata, autoload_with=engine)

mapper_reg = registry()
mapper_reg.map_imperatively(Employee, employees)

print(repr(employees))

stmt = employees.select()
for row in connection.execute(stmt):
    print(row)

stmt = (employees.select().where(employees.c.FirstName == 'Michael'))
for row in connection.execute(stmt):
    print(row)



