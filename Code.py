import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password='1234', database='mysql')

def Menu():
    print("--------------------*********RSG**********---------------------")
    print("###.......WELCOME TO STUDENT MANAGEMENT SYSTEM BY ROHIT.......###")
    print("Enter 1 for adding a new student.")
    print("Enter 2 for displaying the student details.")
    print("Enter 3 for updating the student details.")
    print("Enter 4 for deleting the student details.")
    print("Enter 5 for adding students' examination details.")
    print("Enter 6 for displaying students' examination details.")
    print("Enter 7 for updating student examination details.")
    print("Enter 8 for deleting Student examination details.")
    print("Enter 9 to exit")
    print("----------------------------------------------------------------------------------")

def addstudent():
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM STUDENT WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        print("Roll No already exists. \n")
    else:
        a2 = input("Enter Name-")
        a3 = input("Enter Father's Name-")
        a4 = input("Enter Mother's Name-")
        a5 = input("Enter Address-")
        a6 = int(input("Enter Valid Phone No. (INT)-"))
        a7 = input("Enter E-mail-")
        data = (a1, a2, a3, a4, a5, a6, a7)
        sql = 'INSERT INTO STUDENT VALUES (%s,%s,%s,%s,%s,%s,%s)'
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data entered successfully  \n")

def displaystudent():
    sql = 'SELECT * FROM STUDENT'
    c1 = con.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print("RollNo - {} \nName - {} \nFather's Name - {} \nMother's Name - {} \nAddress - {} \nPhoneNo - {} \nEmail - {}\n".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print("\n")

def updatestudent():
    print("Enter Student Roll no. you want to update-")
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM STUDENT WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        a2 = input("Enter Name-")
        a3 = input("Enter Father's Name-")
        a4 = input("Enter Mother's Name-")
        a5 = input("Enter Address-")
        a6 = int(input("Enter Valid Phone No. (INT)-"))
        a7 = input("Enter E-mail-")
        data = (a2, a3, a4, a5, a6, a7, a1)
        sql = 'UPDATE STUDENT SET Name=%s,FatherName=%s,MotherName=%s,Address=%s,PhoneNo=%s,Email=%s WHERE RollNo=%s'
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data updated successfully \n")
    else:
        print("RollNo doesn't exist \nFirst add the details of the student \n")

def deletestudent():
    print("Enter Student Roll no. you want to delete-")
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM STUDENT WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        data = (a1,)
        sql = "DELETE FROM STUDENT WHERE RollNo=%s"
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data deleted successfully \n")
    else:
        print("RollNo doesn't exist\n")

def addstudentexam():
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM STUDENT WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        a2 = input("Enter Name-")
        a3 = int(input("Enter Class (INT)-"))
        a4 = input("Enter section-")
        a5 = int(input("Enter total marks (INT)-"))
        a6 = int(input("Enter Percentage (INT)-"))
        a7 = input("Enter Grade-")
        data = (a1, a2, a3, a4, a5, a6, a7)
        sql = 'INSERT INTO EXAM VALUES(%s,%s,%s,%s,%s,%s,%s)'
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data entered successfully \n")
    else:
        print("RollNo doesn't exist \nFirst add the details of the student \n")

def displaystudentexam():
    sql = 'SELECT * FROM EXAM'
    c1 = con.cursor()
    c1.execute(sql)
    b = c1.fetchall()
    for i in b:
        print("RollNo - {} \nName - {} \nClass - {} \nSection - {} \nTotal marks - {} \nPercentage - {} \nGrade - {} \n".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print("\n")

def updatestudentexam():
    print("Enter student Roll no you want to update")
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM EXAM WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        a2 = input("Enter Name-")
        a3 = int(input("Enter Class (INT)-"))
        a4 = input("Enter section-")
        a5 = int(input("Enter total marks (INT)-"))
        a6 = int(input("Enter Percentage (INT)-"))
        a7 = input("Enter Grade-")
        data = (a2, a3, a4, a5, a6, a7, a1)
        sql = 'UPDATE EXAM SET Name=%s,Class=%s,Section=%s,TotalMarks=%s,Percentage=%s,Grade=%s WHERE RollNo=%s'
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data updated successfully \n")
    else:
        print("RollNo doesn't exist \nFirst add the details of the student \n")

def deletestudentexam():
    print("Enter Student Roll no. you want to delete-")
    a1 = int(input("Enter Roll No.-"))
    c1=con.cursor()
    c1.execute("SELECT RollNo FROM EXAM WHERE RollNo=%s",(a1,))
    existing=c1.fetchone()
    if existing:
        data = (a1,)
        sql = "DELETE FROM EXAM WHERE RollNo=%s"
        c1 = con.cursor()
        c1.execute(sql, data)
        con.commit()
        print("Data deleted successfully \n")
    else:
        print("RollNo doesn't exist\n")

while True:
    Menu()
    ch = int(input("Enter your choice-"))
    if ch == 1:
        addstudent()
    elif ch == 2:
        displaystudent()
    elif ch == 3:
        updatestudent()
    elif ch == 4:
        deletestudent()
    elif ch == 5:
        addstudentexam()
    elif ch == 6:
        displaystudentexam()
    elif ch == 7:
        updatestudentexam()
    elif ch == 8:
        deletestudentexam()
    elif ch == 9:
        exit()
