import mysql.connector
import datetime

config = {
    'user': 'mj',
    'password': 'Mj1234!.',
    'host': '127.0.0.1',
    'database': 'data_schema',
    'raise_on_warnings': True
}


class Account(object):

    def __init__(self, number):
        self.connection = self.connect()
        sql_account = """
        CREATE TABLE IF NOT EXISTS `account` (
            `id` int NOT NULL AUTO_INCREMENT,
            `number` varchar(26) NOT NULL,
            `balance` decimal(20,2) NOT NULL,
            PRIMARY KEY (`id`));
        """
        self.create_schema(sql_account)

        sql_transaction = """
            CREATE TABLE IF NOT EXISTS `transaction` (
            `id` int NOT NULL AUTO_INCREMENT,
            `account_id` int NOT NULL,
            `time` timestamp NOT NULL,
            `amount` decimal(20,2) NOT NULL,
            PRIMARY KEY (`id`),
            CONSTRAINT `fk_tran_account` FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE);
        """
        self.create_schema(sql_transaction)
        self.number = number
        self.id, self.balance = self.init_account()

    def __del__(self):
        self.disconnect()

    def connect(self):
        try:
            cnx = mysql.connector.connect(**config)
            print("Successfully connected to db")
        except mysql.connector.Error as error:
            print("Unable to connect to database. Err={}".format(error))
            cnx = None
        return cnx

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to db closed")

    def create_schema(self, sql):
        try:
            self.connection.cmd_query(sql)
        except mysql.connector.Error as error:
            print("Failed to execute SQL: {}".format(error))

    def init_account(self):
        retry = 3
        account_sql = "SELECT id, `number`, balance FROM account WHERE `number`=%s"
        account_ins = "INSERT INTO account (`number`, balance) VALUES (%s, %s)"
        ret_id = 0
        ret_balance = 0
        while ret_id == 0 and retry > 0:
            cursor = self.connection.cursor()
            try:
                cursor.execute(account_sql, (self.number,))
                for id, number, balance in cursor:
                    ret_id = id
                    ret_balance = balance

                if ret_id == 0:
                    cursor.execute(account_ins, (self.number, 0))
                    self.connection.commit()

            except mysql.connector.Error as error:
                print("Failed to execute SQL: {}".format(error))
            finally:
                cursor.close()
                retry -= 1

        return ret_id, ret_balance

    def create_transaction(self, amount):
        transaction_sql = "INSERT INTO transaction (account_id, `time`, amount) VALUES (%s, %s, %s);"
        balance_sql = """UPDATE account SET balance = (SELECT SUM(amount) FROM transaction
                        WHERE account_id = %s) WHERE id = %s;
                        """
        cursor = self.connection.cursor()
        try:

            cursor.execute(transaction_sql, (self.id, datetime.datetime.now(), amount))
            cursor.execute(balance_sql, (self.id, self.id))
            self.connection.commit()
        except mysql.connector.Error as error:
            print("Failed to execute SQL: {}".format(error))
            self.connection.rollback()
        finally:
            cursor.close()

        return True

    def __str__(self):
        return "Account: number={} id={} balance={}".format(self.number, self.id, self.balance)

    def deposit(self, amount):
        if amount > 0:
            if self.create_transaction(amount):
                self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            if self.create_transaction(-amount):
                self.balance -= amount


account = Account('15102010450000998000013422')
print(account)
account.deposit(5)
print(account)
account.deposit(15)
print(account)
account.withdraw(20)
print(account)
account.disconnect()
