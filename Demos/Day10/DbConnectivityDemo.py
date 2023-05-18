#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root")
#step2
cur=mydb.cursor()
#step 3
cur.execute("show databases")

for db in cur:
    print(db)
    
#step4
cur.close()
mydb.close()


# In[2]:


#creating Database
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root")
#step2
cur=mydb.cursor()
#step 3
cur.execute("create database mytest")
cur.execute("show databases")
for db in cur:
    print(db)
    
#step4
cur.close()
mydb.close()


# In[3]:


#creating Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
cur.execute("create table book(bookid int auto_increment primary key,name varchar(200),author varchar(200), price float(6,2))")
cur.execute("show tables")
for db in cur:
    print(db)
    
#step4
cur.close()
mydb.close()


# In[4]:


#Insert record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
cur.execute("insert into book(name ,author , price ) values('let us c','Kanitkar',500.00)")
mydb.commit()
print(cur.rowcount," inserted Successfully")

#step4
cur.close()
mydb.close()


# In[5]:


#Insert record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
name= input("Enter book Name")
author= input("Enter book author")
price= float(input("Enter book price"))

sql="insert into book(name ,author , price ) values(%s,%s,%s)"
val=(name,author,price)

cur.execute(sql,val)

mydb.commit()
print(cur.rowcount," inserted Successfully")

#step4
cur.close()
mydb.close()


# In[6]:


#Insert record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3


sql="insert into book(name ,author , price ) values(%s,%s,%s)"
lst=[]
for i in range(0,3):
    name= input("Enter book Name")
    author= input("Enter book author")
    price= float(input("Enter book price"))
    lst.append((name,author,price))


cur.executemany(sql,lst)

mydb.commit()
print(cur.rowcount," inserted Successfully")

#step4
cur.close()
mydb.close()


# In[9]:


#select record from Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
cur.execute("select * from book")
lst = cur.fetchall()
for l in lst:
    print(l)
#step4
cur.close()
mydb.close()


# In[11]:


#Insert record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
cur.execute("select * from book")
lst = cur.fetchmany(3)
for l in lst:
    print(l)
#step4

mydb.close()


# In[12]:


#Insert record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
cur.execute("select * from book")
lst = cur.fetchone()
print(lst)
#step4

mydb.close()


# In[13]:


#Update record Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3


sql="Update book set price=%s where bookid=%s"
val=(1000,2)

cur.execute(sql,val)

mydb.commit()
print(cur.rowcount," Updated Successfully")

#step4
cur.close()
mydb.close()


# In[15]:


#Delete record from Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3


sql="Delete from book where bookid=%s"
val=(3,)

cur.execute(sql,val)

mydb.commit()
print(cur.rowcount," Deleted Successfully")

#step4
cur.close()
mydb.close()


# In[ ]:


#Drop Table
import mysql.connector
#step 1
mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="mytest")
#step2
cur=mydb.cursor()
#step 3
sql="drop table book"
cur.execute(sql)
print(cur.rowcount," Drop Successfully")
#step4
cur.close()
mydb.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




