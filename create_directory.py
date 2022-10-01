import os

dir = "fsystem"
dir1 = "slash"
str(dir1)
sub_dir = ['boot','root','home','etc','bin']

os.mkdir(dir)
new = os.path.join(dir,dir1)
os.mkdir(new)
for i in sub_dir:
    path = os.path.join(new, i)
    os.mkdir(path)

