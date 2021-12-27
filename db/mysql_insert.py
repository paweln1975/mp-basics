import mysql.connector

config = {
    'user': 'mj',
    'password': 'Mj1234!.',
    'host': '127.0.0.1',
    'database': 'data_schema',
    'raise_on_warnings': True
}


def delete_test_data(cnx, _id):
    cursor = cnx.cursor()
    record_found = False
    try:
        mysql_delete_query = "DELETE FROM author WHERE id > %s;"
        cursor.execute(mysql_delete_query, (_id,))
        if cursor.rowcount >= 1:
            record_found = True
        cnx.commit()
    except mysql.connector.Error as error:
        print("Failed to DELETE from MySQL table {}".format(error))
    finally:
        cursor.close()
    return record_found


def check_if_exists(cnx, first_name, last_name):
    cursor = cnx.cursor()
    record_found = False
    try:
        mysql_select_query = "SELECT * FROM author WHERE first_name=%s AND last_name=%s;"
        record = (first_name, last_name)
        cursor.execute(mysql_select_query, record)
        if len(cursor.fetchall()) >= 1:
            record_found = True
    except mysql.connector.Error as error:
        print("Failed to SELECT from MySQL table {}".format(error))
    finally:
        cursor.close()
    return record_found


def insert_author(cnx, first_name, last_name):
    if check_if_exists(cnx, first_name, last_name):
        print(f"Record already exists with values ({first_name}, {last_name})")
        return False

    cursor = cnx.cursor()
    try:
        mysql_insert_query = "INSERT INTO author (first_name, last_name) VALUES (%s, %s);"
        record = (first_name, last_name)
        cursor.execute(mysql_insert_query, record)
        cnx.commit()
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        print(f"Record inserted with values ({first_name}, {last_name})")
        cursor.close()
    return True


def connect():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as error:
        print("Unable to connect to database. Err={}".format(error))
        cnx = None
    return cnx


def disconnect(cnx):
    if cnx.is_connected():
        cnx.close()
        print("MySQL connection is closed")


connection = connect()
if connection:
    delete_test_data(connection, 4)
    insert_author(connection, "Bob", "Dylan")
    insert_author(connection, "Mike", "Jordan")
    disconnect(connection)
