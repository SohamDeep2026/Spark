DROP database if exists lib_mng_db;
CREATE database lib_mng_db;
USE lib_mng_db;

DROP table if exists User_Details;
CREATE TABLE User_Details
(	Username	varchar(30) primary key,
	U_Name	varchar(30)	not null,
	About	varchar(100),
    U_Type	varchar(6)	not null,
    Date_of_joining	date,
    U_Password	varchar(30) not null
);

DROP table if exists Books;
CREATE TABLE Books
(	Book_ID	integer primary key,
	Book_Title	varchar(100)	not null,
    Author_Name	varchar(100),
	Genre	varchar(50),
    Number_of_Copies	integer	not null	default(0),
    Number_of_Available_Copies	integer	not null	default(0)
);

DROP table if exists User_Books;
CREATE TABLE User_Books
(	User_Book_ID	integer   auto_increment    primary key,
	Username	varchar(30)	not null references User_Details(Username),
    Book_ID	integer not null references Books(Book_ID),
	Issued_Date	date	not null,
    Return_date	date	default(null)
);

insert into User_Details(Username, U_Name, About, U_Type, Date_of_Joining, U_Password) 
values("Admin001", "Shanta Mukherjee", "Head Librarian", 
"Admin", curdate(), "HopscotchLib");

alter table User_Books auto_increment = 100;