create database terminal_project;
user terminal_project;

drop table passwd;
drop table group1;

create table group1( gid int auto_increment,
                     group_name varchar(45) unique,
                     password_linked_gshadow varchar(8),
                     group_members varchar(45),
                     primary key(gid)
 );


alter table group1 auto_increment=1000;


create table g_shadow( group_name varchar(45) unique,
                       encrypted_password varchar(8),
                       administrators varchar(45),
                       members varchar(45),
                       foreign key(group_name) references group1(group_name)
 );

create table passwd( uid int primary key auto_increment,
                     user_name varchar(45) unique,
                     gid int,
                     comment varchar(45),
                     home_directory varchar(45) not null default '/home/dir',
                     default_shell varchar(45) not null default '/bin/bash',
                     foreign key(gid) references group1(gid)
 );


alter table passwd auto_increment=1000;

create table p_shadow(user_name varchar(45) unique,
                      encrypted_password varchar(8),
                      last_password_change date,
                      maximum int,
                      minimum int,
                      warn int,
                      inactive int,
                      expire date,
                      foreign key(user_name) references passwd(user_name)
 );


