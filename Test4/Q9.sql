create database eleven;
use eleven;

create table book(
	bookid int,
    bookname varchar(100),
    author varchar(100),
    price int);
    
insert into book(bookid , bookname , author , price)
values
	( 1 , 'Python Basics' , 'John' , 500),
	( 2 , 'Learning SQL' , 'David' , 700);



