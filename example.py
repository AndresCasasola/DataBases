import mysql.connector

connector = mysql.connector.connect(host='localhost', user='root', passwd='password', database='world')

cursor = connector.cursor()
cursor.execute("SELECT * FROM city WHERE Name='Madrid' ")
data = cursor.fetchall()

for row in data:
    print(row)
