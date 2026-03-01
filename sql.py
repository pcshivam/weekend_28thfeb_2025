import sqlite3
connection = sqlite3.connect("CREATE DATABASE geeks.db")
cursor = connection.cursor()
print(cursor)
cursor.execute("CREATE TABLE IF NOT EXISTS employee (ID INTEGER, name TEXT, salary INTEGER)")
cursor.execute("INSERT INTO employee VALUES (1001, 'Shivam', 35000)")
cursor.execute("SELECT * FROM employee")