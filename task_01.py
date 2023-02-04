import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE my_first_db")

my_cursor.close()
mydb.close()
