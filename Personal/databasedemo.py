import mysql.connector

#To create database
#mydb=mysql.connector.connect(host="localhost",user="root",password="root")
#cur.execute("create database mytest")
#cur.execute("show databases")

#After databse is created use below line
mydb = mysql.connector.connect(host="localhost", user="root", password="Always&Forever", database="mytest")

#Creating object of cursor
cur = mydb.cursor()


#Create Table
#cur.execute("create table book(bookid int auto_increment primary key,name varchar(200),author varchar(200), price float(6,2))")
#cur.execute("show tables")


#Inserting Records to table
#cur.execute("insert into book(name, author, price) values ('Business Analytics', 'James R. Evans', 900.00)")

#sql="insert into book(name ,author , price ) values(%s,%s,%s)"
#lst = []
#for i in range(0,4):
#    name = input("Enter book Name")
#    author = input("Enter book author")
#    price = float(input("Enter book price"))
#    lst.append((name, author, price))

#cur.executemany(sql,lst)

#mydb.commit()
#print(cur.rowcount," inserted Successfully")




#Fetching all records from table
#cur.execute("select * from book")
#lst=cur.fetchall()
#for i in lst:
#    print(i)

#Another Way to fetch records and for using this don't close the cursor
#cur.execute("select * from book")
#lst=cur.fetchmany(3)
#for i in lst:
#    print(i)

#Way to fecth first record and for using this don't close the cursor
#cur.execute("select * from book")
#lst = cur.fetchone()
#print(lst)


#Update values to table
#sql="Update book set price=%s where bookid=%s"
#val=(1000,2)
#cur.execute(sql,val)
#mydb.commit()
#print(cur.rowcount," Updated Successfully")



#Delete Record From table
#sql="Delete from book where bookid=%s"
#val=(3,)
#cur.execute(sql,val)
#mydb.commit()
#print(cur.rowcount," Deleted Successfully")


#Drop Table
#sql="drop table book"
#cur.execute(sql)
#print(cur.rowcount," Drop Successfully")



#for db in cur:
#    print(db)

cur.close()
mydb.close()
