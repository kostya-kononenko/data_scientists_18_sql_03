import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="my_first_db"
)

my_cursor = mydb.cursor()
info_for_insert = "INSERT INTO student (id, name) VALUES (%s, %s)"
new_data = (1, "John")
my_cursor.execute(info_for_insert, new_data)
mydb.commit()
my_cursor.close()

my_cursor = mydb.cursor()
info_for_insert = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
new_data = (1, "John", 10000)
my_cursor.execute(info_for_insert, new_data)
mydb.commit()
