import mysql.connector

# Before Creating Database use below line
# mydb = mysql.connector.connect(host="localhost", user="root", password="Always&Forever")

# After creating Database
mydb = mysql.connector.connect(host="localhost", user="root", password="Always&Forever", database="student")

cur = mydb.cursor()

# Created Database Student
# cur.execute("create database student")
# cur.execute("show Databases")

# 1. Create Table Student2
# cur.execute("create table student2(roll_no int primary key, name varchar(30), marks float(10,2))")
# cur.execute("show tables")


# 2. Insert Records into table
# sql = "insert into student2(roll_no, name ,marks) values(%s,%s,%s)"
# lst = []
# for i in range(0,5):
#    roll_no = int(input('Enter Roll No: '))
#    name = input('Enter Name: ')
#    marks = float(input('Enter Marks: '))
#    lst.append((roll_no, name, marks))

# cur.executemany(sql, lst)
# mydb.commit()
# print(cur.rowcount," inserted Successfully")


# 3. Updating Values in Table
# sql="Update student2 set marks=%s where name=%s"
# val = (78.00, "Rama")
# cur.execute(sql,val)
# mydb.commit()
# print(cur.rowcount," Updated Successfully")


# 4. Display All Records
# cur.execute("select * from student2")
# lst = cur.fetchall()
# for i in lst:
#   print(i)


# 5. Display records who score more than 80
# cur.execute("select * from student2 where marks > 80.00")
# lst = cur.fetchall()
# for i in lst:
#    print(i)


# 6. Display students whose name starts with R
# cur.execute("select * from student2 where name LIKE 'R%' ")
# lst = cur.fetchall()
# for i in lst:
#    print(i)


# for db in cur:
#    print(db)


cur.close()
mydb.close()
