import mysql.connector

config = {
    'user': 'mj',
    'password': 'Mj1234!.',
    'host': '127.0.0.1',
    'database': 'data_schema',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = "SELECT id, first_name, last_name FROM author order by last_name"

cursor.execute(query)

for (id, first_name, last_name) in cursor:
    print(f"{id}:{first_name}, {last_name}")

cursor.close()
cnx.close()
