import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="terminal_project"
)

mycursor = mydb.cursor()
clist=['useradd']
olist=['-g','-G']
alist=[]
ulist=[]
cmd_list = []
shell='[ root@localhost ~ ] # '

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
  useradd_cmd()

def useradd_cmd():
  if len(cmd_list)==4:
    if cmd_list[0] =='useradd' and cmd_list[1] =='-g' and cmd_list[2] in alist :
      insert_group = "INSERT INTO passwd (user_name,gid) values (%s,%s)"
      gid_list = []
      sql = "SELECT gid from group1 where group_name = %s"
      val0 = [cmd_list[2]]
      mycursor.execute(sql,val0)
      for i in mycursor:
        gid_no = str(list(i))
        gid_list.append(gid_no[1:-1])
      
      val = [cmd_list[3],gid_list[0]]
      mycursor.execute(insert_group,val)
      mydb.commit()
      bash_shell()
  
      #useradd_cmd()
    #useradd_cmd()

    elif cmd_list[0] =='useradd' and cmd_list[1] =='-g' and cmd_list[2] in alist and cmd_list[3] in ulist :
      print("useradd: user '"+cmd_list[1]+"' already exists")
      bash_shell()
      #useradd_cmd()
    #useradd_cmd()

    elif cmd_list[0] =='useradd' and cmd_list[1] =='-g' and cmd_list[2] not in alist :
      print ("useradd: group '"+cmd_list[2]+"' does not exist") 
      bash_shell()
      #useradd_cmd()
    #useradd_cmd()
  #useradd_cmd()

  elif len(cmd_list)==2:
    if cmd_list[0] =='useradd':
      # for adding group
      insert_group = "INSERT INTO group1 (group_name) values (%s)"
      val1 = [cmd_list[1]]
      mycursor.execute(insert_group,val1)
      mydb.commit()

      # for adding user
      insert_user = "INSERT INTO passwd (user_name,gid) values (%s,%s)"
      gid_list=[]
      sql = "SELECT gid from group1 where group_name = %s"
      val2 = [cmd_list[1]]
      mycursor.execute(sql,val2)
      for i in mycursor:
        gid_no=str(list(i))
        gid_list.append(gid_no[1:-1])

      
      val3 = [cmd_list[1],gid_list[0]]
      mycursor.execute(insert_user,val3)
      mydb.commit()
      bash_shell()
      #useradd_cmd()
    #useradd_cmd()

    elif cmd_list[0] == 'useradd' and cmd_list[1] in ulist:
      print("useradd: user '"+cmd_list[1]+"' already exists")
      bash_shell()
      #useradd_cmd()

    
    elif cmd_list[0] != 'useradd':
      print("bash: "+cmd_list[0]+" : command not found")
      bash_shell()
      #useradd_cmd()

bash_shell()
#useradd_cmd()