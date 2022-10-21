import cmd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="terminal_project"
)
# def variables():
mycursor = mydb.cursor()
clist=['useradd','groupadd','id']
olist=['-g','-G']
alist=[]
ulist=[]
cmd_list = []
shell='[ root@localhost ~ ] # '


def user_group_list():
    mycursor.execute('SELECT group_name from group1;')
    for i in mycursor:
      gname=str(list(i))
      alist.append(gname[2:-2])
    mycursor.execute('SELECT user_name from passwd;')
    for i in mycursor:
      uname=str(list(i))
      ulist.append(uname[2:-2])

def bash_shell():
  s = str(input(shell))
  for i in s.split():
    cmd_list.append(i)

def commands():
  alist.clear()
  ulist.clear()
  while 1>0:
    user_group_list()
    bash_shell()
    useradd_cmd()

def useradd_cmd():
  if len(cmd_list)==4:
    if cmd_list[0] =='useradd' and (cmd_list[1] =='-g' or cmd_list[1] == '-G') and cmd_list[2] in alist and cmd_list[3] not in ulist :
      insert_group = "INSERT INTO passwd (user_name,gid,home_directory) values (%s,%s,%s)"
      gid_list = []
      sql = "SELECT gid from group1 where group_name = %s"
      val0 = [cmd_list[2]]
      mycursor.execute(sql,val0)
      for i in mycursor:
        gid_no = str(list(i))
        gid_list.append(gid_no[1:-1])
      val = [cmd_list[3],gid_list[0],"/home/"+cmd_list[3]]
      mycursor.execute(insert_group,val)
      mydb.commit()
      cmd_list.clear()
      commands()
    elif cmd_list[0] =='useradd' and (cmd_list[1] =='-g' or cmd_list[1] == '-G') and cmd_list[2] in alist and cmd_list[3] in ulist :
      print("useradd: user '"+cmd_list[3]+"' already exists")
      cmd_list.clear()
      commands()
    elif cmd_list[0] =='useradd' and (cmd_list[1] =='-g' or cmd_list[1] == '-G') and cmd_list[2] not in alist :
      print ("useradd: group '"+cmd_list[2]+"' does not exist") 
      cmd_list.clear()
      commands()
    #elif cmd_list[0] == 'groupadd' and 
    elif cmd_list[0] not in clist:
      print("bash: "+cmd_list[0]+" : command not found")
      cmd_list.clear()
      commands()
   # continue
  elif len(cmd_list)==2:
    if cmd_list[0] =='useradd' and cmd_list[1] not in ulist:
      # for adding group
      insert_group = "INSERT INTO group1 (group_name) values (%s)"
      val1 = [cmd_list[1]]
      mycursor.execute(insert_group,val1)
      mydb.commit()
      # for adding user
      insert_user = "INSERT INTO passwd (user_name,gid,home_directory) values (%s,%s,%s)"
      gid_list=[]
      sql = "SELECT gid from group1 where group_name = %s"
      val2 = [cmd_list[1]]
      mycursor.execute(sql,val2)
      for i in mycursor:
        gid_no=str(list(i))
        gid_list.append(gid_no[1:-1])
      val3 = [cmd_list[1],gid_list[0],"/home/"+cmd_list[1]]
      mycursor.execute(insert_user,val3)
      mydb.commit()
      cmd_list.clear()
      commands()
    elif cmd_list[0] == 'useradd' and cmd_list[1] in alist :
      print("useradd: group "+cmd_list[1]+" exists - if you want to add this user to that group, use -g.")
      cmd_list.clear()
      commands()
    elif cmd_list[0] == 'useradd' and cmd_list[1] in ulist:
      print("useradd: user '"+cmd_list[1]+"' already exists")
      cmd_list.clear()
      commands()
    elif cmd_list[0] == 'groupadd' and cmd_list[1] not in alist:
      # for adding group
      insert_group = "INSERT INTO group1 (group_name) values (%s)"
      val1 = [cmd_list[1]]
      mycursor.execute(insert_group,val1)
      mydb.commit()
      cmd_list.clear()
      commands()
    elif cmd_list[0] == 'groupadd' and cmd_list[1] in alist:
      print("groupadd: group '"+cmd_list[1]+"' already exists")
      cmd_list.clear()
      commands()
    elif cmd_list[0] not in clist:
      print("bash: "+cmd_list[0]+" : command not found")
      cmd_list.clear()
      commands()


commands()
