import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="project",
  password="Redhat@123",
  database="mydatabase"
)

#
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase1")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("CREATE TABLE passwd (uname VARCHAR(255), encrypt_pass varchar(10), uid int(10),gid int(10),home_dir varchar(255),shell varchar(255))")

mycursor.execute('SHOW TABLES;')
for x in mycursor:
  print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "")
mycursor.execute(sql, val)

mydb.commit()
f = open("demofile2.txt", "a")
f.write(val[0]+":"+val[1]+":"+"something\t")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


print(mycursor.rowcount, "record inserted.")

mycursor.execute('select * from customers;')
for x in mycursor:
  print(x)