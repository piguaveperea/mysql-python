create database if not exists db_test;
use db_test;

# __nombre_atributo __tipo__ 
create table if not exists casa (
	id int primary key auto_increment,
    forma varchar(40) not null,
    color varchar(40) not null
)
