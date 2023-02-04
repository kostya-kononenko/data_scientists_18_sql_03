import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="my_first_db"
)

my_cursor = mydb.cursor()
my_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

my_cursor.close()
mydb.close()
