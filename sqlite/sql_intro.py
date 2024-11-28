from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import registry





class Building(object):
    __tablename__ = 'buildings'

    def __init__(self, counter, address):
        self.counter = counter
        self.address = address

engine = create_engine('sqlite:///Buildings_Database.sqlite', echo=True)
connection = engine.connect()

metadata = MetaData()
buildings = Table('Buildings', metadata, autoload_with=engine)

mapper_reg = registry()
mapper_reg.map_imperatively(Building, buildings)


print(repr(buildings))
stmt = buildings.select().where(buildings.c.address == 'Green Street, 4')
for row in connection.execute(stmt):
    print(row)