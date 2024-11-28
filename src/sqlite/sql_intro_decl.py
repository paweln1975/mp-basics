from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select

mapper_registry = registry()


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employees"

    EmployeeId: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str] = mapped_column(nullable=False)
    LastName: Mapped[str] = mapped_column(nullable=False)
    Title: Mapped[str] = mapped_column(nullable=False)
    ReportsTo: Mapped[int] = mapped_column(ForeignKey("employees.EmployeeId"))
    ReportsToParent: Mapped["Employee"] = relationship()
    # Reporters = relationship("Employee", back_populates="ReportsTo")


engine = create_engine('sqlite:///chinook.db', echo=True)
session = Session(engine)

session.add(Employee(FirstName='Pawel', LastName='Niedziela'))
session.commit()

stmt = (
    select(Employee).where(Employee.LastName == "Niedziela")
)
for user in session.scalars(stmt):
    print(user.EmployeeId, user.FirstName, user.LastName, user.Title, user.ReportsTo)

stmt = select(Employee).where(Employee.FirstName == "Pawel")
p = session.scalars(stmt)
for pawel in p:
    pawel.FirstName = "Piotr"

session.commit()

stmt = select(Employee).where(Employee.LastName == "Niedziela")
for row in session.scalars(stmt):
    session.delete(row)
session.commit()
