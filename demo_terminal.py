import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="project",
  password="Redhat@123",
  database="terminal_project"
)

mycursor = mydb.cursor()


#val = []
#mycursor.execute(sql, val)
uid = [1000,1001,1002,1003,1004,1005]
gid = [1000,1001,1002,1003,1004,1005]



mydb.commit()

def write_to_file():
    f = open("passwd", "a")
    f.write(val[0]+":"+val[1]+":"+val[2]+":"+val[3]+":"+val[4]+":"+val[5]+"\t")
    f.close()

def read_file():
    #open and read the file after the appending:
    f = open("demofile2.txt", "r")
    print(f.read())

root_user = 'root'
root_pass = 'root'
hostname = 'localhost'

login_user = input(hostname+" login : ")
login_pass = input("password : ")

sign = ['$','#']
shell = "["+login_user+"@"+hostname+" ~ ] "

if login_user == 'root' and login_pass == 'root':
    login_shell = shell+sign[1]+" "
    # doing something useless
    command = input(login_shell)
    user_name = input("enter user name : ")
    home_directory = "/home/"+user_name
    default_shell = "/bin/bash"

    if command == 'useradd':
        for i in uid:
            sql = "INSERT INTO passwd (uname not null, uid not null,gid not null,comment,home_dir not null,default_shell not null) VALUES (%s, %s,%s,%s,%s,%s)"
            val = (user_name,uid[i],gid[i],"",home_directory,default_shell)
        mycursor.execute(sql, val)
        mycursor.commit()
        write_to_file()

        

else :
    print("invalid login")