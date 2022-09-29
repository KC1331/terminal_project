import os

dir = "a"
sub_dir = ['boot','root','home','etc','bin']

os.mkdir(dir)
for i in sub_dir:
    path = os.path.join(dir, i)
    os.mkdir(path)

