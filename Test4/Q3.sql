create database five;
use five;

create table product(
	productid int,
    productname varchar(100),
    category varchar(100),
    price int
);

insert into product(productid , productname , category, price)
values
	( 1 , 'Mouse' , 'Electronics' , 800 ),
	(2 , 'Laptop' , 'Electronics' , 65000),
	(3 , 'Chair' , 'Furniture',  4500 ),
	(4 , 'Keyboard' , 'Electronics' , 1200);

select * from product;

select * from product where price > 1000;

select * from product where category = 'electronics';

select * from product where productname = 'Laptop';

