import datetime
import pytz


class Account:
    """Simple account implementation"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, number, balance=0):
        self.__balance = balance
        self._transaction_list = []
        if balance > 0:
            self._transaction_list.append((Account._current_time(), balance))
        self.number = number
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            self.show_balance()
        else:
            print("Amount must be greater then 0")

    def withdraw(self, amount):
        if amount < 0:
            print("Amount must be greater then 0")

        if self.__balance - amount > 0:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
            self.show_balance()
        else:
            print(f"Amount balance must be greater then {amount} but is {self.__balance}")

    def show_balance(self):
        print(f"Balance for account ({self.number}) after operation: {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdrawn"
                amount *= -1

            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    a = Account("8383", 5)
    print(a.__dict__)   # pay attention to the name _Account__balance
    a.__balance = 500
    print(a.__dict__)
    a.deposit(10)
    a.withdraw(5)
    a.withdraw(10)
    a.show_transactions()
