import os
import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "receipt.db")

# Create a connection witn databse
with sqlite3.connect("receipt.db") as db:
  cursor = db.cursor()
  if cursor != 0:
    print("Connection Successful")
  else:
    print('Connection Failed')
    exit()

cursor.execute('''SELECT * FROM details''')

myresult = cursor.fetchall()

for x in myresult:
  print("Bank Receipt Details: ",x)


cursor.execute('''select MAX(salary) from details''')

mysal =  cursor.fetchone()

for y in mysal:
  print("Highest Salary: ",y)



