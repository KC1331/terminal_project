'''uid=[1,2,3,45,5]
gid=[2,3,45,5]

for i in (uid):
    print(uid[i])'''

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="project",
  password="Redhat@123",
  database="terminal_project"
)

shell = "[root@localhost ~ ] # "
uid = [1000,1001,1002,1003,1004,1005]
gid = [1000,1001,1002,1003,1004,1005]

for i in uid:
    cmd,name = input(shell),input(shell)
    gid=uid
    sql = "INSERT INTO passwd (uname, uid,gid,comment,home_dir,default_shell ) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name,i,i,"","/home/"+name,"/bin/bash")
    mycursor = mydb.cursor()
    mycursor.execute(sql,val)

mydb.commit()