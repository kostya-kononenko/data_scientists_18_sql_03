import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="my_first_db"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

my_cursor.close()
mydb.close()
