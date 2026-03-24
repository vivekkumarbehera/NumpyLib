#Database Connect
import mysql.connector as mysql
my_db = mysql.connect(host="localhost", user="root", password="pass123")
my_cursor = my_db.cursor()
'''
try:
    my_db = mysql.connect(host="localhost", user="root", password="pass123")
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS Cricket11")
    my_cursor.execute("USE Cricket11")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS players (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, role VARCHAR(255))")
    print("Database and table created successfully!")

    my_cursor.execute("SELECT * FROM players")
    result = my_cursor.fetchall()
    print("Players in the table:", result)
    my_db.close()
except mysql.Error as err:
    print(f"Error: {err}")
'''
#insert data into table
my_cursor.execute("USE Cricket11")
'''data=[("Virat Kohli", 33, "Batsman"), ("Rohit Sharma", 34, "Batsman"), ("Jasprit Bumrah", 32, "Bowler")]
for i in data:
    my_cursor.execute("INSERT INTO players (name, age, role) VALUES (%s, %s, %s)", i)
my_db.commit()
print("Data inserted successfully!")'''
#update data in table
my_cursor.execute("UPDATE players SET age = 35 WHERE name = 'Rohit Sharma'")
my_db.commit()
print("Data updated successfully!")
