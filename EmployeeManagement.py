import sqlite3

conn = sqlite3.connect('database1.db')
c = conn.cursor()


def create_profsnltable():
    c.execute(
        'CREATE TABLE IF NOT EXISTS profsnltable2(EMP_NO INTEGER PRIMARY KEY check(EMP_NO<1000),EMP_NAME TEXT NOT NULL,HIREDATE TEXT NOT NULL,JOB_TITLE TEXT check(JOB_TITLE in ("MANAGER","CLERK","WORKER","INCHARGE")),SALARY INTEGER CHECK(SALARY>5000 AND SALARY<50000),DEPT_ID INTEGER UNIQUE,DPT_NAME TEXT check(DPT_NAME in("FINISHING","MARKETING","ADMINISTRATION","SALES","PURCHASING","IT","HUMAN RESOURCES","PUBLIC RELATIONS")))')


def empinfo():
    l = []
    c.execute("select * from profsnltable2")
    for i in c.fetchall():
        l.append(i[0])
    return l


def profsnldata_entry():
    empno = int(input("Enter employee_no.:"))
    l1 = empinfo()
    if (empno in l1):
        print("  Employee no.is already existed!!!")
    else:
        ename = input("Enter name of employee:")
        date_entry = input("Enter hiredate of a employee:")
        job = input("Enter job_title of a employee:")
        salary = int(input("Enter salary of a employee:"))
        dep_id = int(input("Enter dept_id of a employee:"))
        dep_name = input("Enter dept_name of a employee:")
        c.execute("INSERT INTO profsnltable2 VALUES(?,?,?,?,?,?,?)",
                  (empno, ename, date_entry, job, salary, dep_id, dep_name))
        print(" Insertion of data is completely succesful")


def select_profsnltable():
    print(
        '\n\tSELECT DATA:\n Enter[1] to view professional details of all employee\n Enter[2] to view professional detail of a employee')
    y = int(input("Enter ur choice"))
    if (y == 1):
        c.execute("select * from profsnltable2")
        for i in c.fetchall():
            print(i)
    elif (y == 2):
        new = int(input("Enter employee no. whose detail u want to view"))
        c.execute('select * from profsnltable2 where EMP_NO=?', (new,))
        print(c.fetchone())
    else:
        print("OOPS! u have entered wrong choice")


def updateprofsnl():
    print(
        "\n UPDATE:\nEnter[1] to update all details of a employee\nEnter[2] to update specific detail of a employee\n")
    y = int(input("Enter ur choice"))
    if (y == 1):
        new_no = int(input("Enter employee no whose detail u want to update"))
        l1 = empinfo()
        if (new_no in l1):
            new_name = input("Enter new name of a employee:")
            new_date = input("Enter new hiredate of a employee:")
            new_job = input("Enter new job_title of a employee:")
            new_salary = int(input("Enter new salary of a employee:"))
            new_dep_id = int(input("Enter new departmnt id of a employee:"))
            new_dep_name = input("Enter new department name of a employee:")
            c.execute(
                'UPDATE profsnltable2 set EMP_NAME=?,HIREDATE=?,JOB_TITLE=?,SALARY=?,DEPT_ID=?,DPT_NAME=? where EMP_NO=?',
                (new_name, new_date, new_job, new_salary, new_dep_id, new_dep_name, new_no))
            print("   Detail of a employee is updated")
        else:
            print("  Employee no. is not existed!!")
    elif (y == 2):
        v = int(input(
            "UPDATE:\nEnter[1] to update employee name\nEnter[2] to update hiredate of employee\nEnter[3] to update job_title of a employee\nEnter[4] to update salary of a employee\nEnter[5] to update departmnt id of a employee\nEnter[6] to update departmnt name of a employee\n"))
        if (v == 1):
            new_no = int(input("Enter employee no whose name u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = input("Enter a new name")
                c.execute('UPDATE profsnltable2 set EMP_NAME=? where EMP_NO=?', (new, new_no))
            else:
                print("  Employee no is not existed")
        elif (v == 2):
            new_no = int(input("Enter employee no. whose date_entry u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = input("Enter a new hiredate")
                c.execute('UPDATE profsnltable2 set HIREDATE=? where EMP_NO=?', (new, new_no))
            else:
                print("  Employee no. is not existed!!")
        elif (v == 3):
            new_no = int(input("Enter employye no. whose job u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = input("Enter a new job")
                c.execute('UPDATE profsnltable2 set JOB_TITLE=? where EMP_NO=?', (new, new_no))
            else:
                print("  Employee no. is not existed!!")
        elif (v == 4):
            new_no = int(input("Enter employee no. whose salary u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = int(input("Enter a new salary:"))
                c.execute('UPDATE profsnltable2 set SALARY=? where EMP_NO=?', (new, new_no))
            else:
                print(" Employee no. is not existed!!")

        elif (v == 5):
            new_no = int(input("Enter employee no. whose departmnt id u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = int(input("Enter a new deptartmnt id"))
                c.execute('UPDATE profsnltable2 set DEPT_ID=? where EMP_NO=?', (new, new_no))
            else:
                print(" Employee no. is not existed!!")
        elif (v == 6):
            new_no = int(input("Enter employee no. whose departmnt name u want to update"))
            l1 = empinfo()
            if (new_no in l1):
                new = input("Enter a new deptartmnt name")
                c.execute('UPDATE profsnltable2 set DPT_NAME=? where EMP_NO=?', (new, new_no))
            else:
                print(" Employee no. is not existed!!")
        else:
            print("OOPS! u have entered wrong choice")
    else:
        print("OOPS! u have entered wrong choice")


def delete_profsnltable():
    id = int(input("Enter employee no. whose data u want to delete"))
    l1 = empinfo()
    if (id in l1):
        c.execute('DELETE from profsnltable2 where EMP_NO=?', (id,))
        print("detail of a employee is deleted")
    else:
        print(" Employee no. is not existed!!")


def create_prsnltable():
    c.execute(
        'CREATE TABLE IF NOT EXISTS prsnltable3(EMP_NO INTEGER NOT NULL CHECK(EMP_NO<1000),E_ID INTEGER PRIMARY KEY,AGE INTEGER CHECK(AGE>22 AND AGE<60),MOBILE_NO INTEGER,ADDRESS TEXT,CITY TEXT NOT NULL,FOREIGN KEY (EMP_NO) REFERENCES profsnltable1 (EMP_NO))')


def insert_prsnltable():
    empno = int(input("Enter employee_no.:"))
    eid = int(input("Enter employee id:"))
    age = int(input("Enter age of a employee:"))
    mobile = int(input("Enter mobile_no of a employee:"))
    adress = input("Enter address of a employee:")
    city = input("Enter city of a employee:")
    c.execute("INSERT into prsnltable3 VALUES(?,?,?,?,?,?)", (empno, eid, age, mobile, adress, city))


def select_prsnltable():
    print(
        '\n\tVIEW DATA:\n Enter[1] to view personal details of all employee\n Enter[2] to view personal detail of a employee')
    y = int(input("Enter ur choice:"))
    if (y == 1):
        c.execute("select * from prsnltable3")
        for i in c.fetchall():
            print(i)
    elif (y == 2):
        new = int(input("Enter employee no. whose personal detail u want to view"))
        c.execute('select * from prsnltable3 where EMP_NO=?', (new,))
        print(c.fetchone())
    else:
        print("OOPS! u have entered wrong choice")


def update_prsnltable():
    print(
        "\n UPDATE:\nEnter[1] to update all personal details of a employee\nEnter[2] to update specific personal detail of a employee\n")
    y = int(input("Enter ur choice"))
    if (y == 1):
        new_no = int(input("Enter employee no whose detail u want to update"))
        new_id = int(input("Enter new e_id:"))

        new_age = int(input("Enter new age:"))
        new_mobile = int(input("Enter new mobile_no:"))
        new_addrs = input("Enter new address :")
        new_city = input("Enter new city :")
        c.execute('UPDATE prsnltable3 set E_ID=?,AGE=?,MOBILE_NO=?,ADDRESS=?,CITY=? where EMP_NO=?',
                  (new_id, new_age, new_mobile, new_addrs, new_city, new_no))
    elif (y == 2):
        v = int(input(
            "UPDATE:\nEnter[1] to update employee age\nEnter[2] to update mobile_no of employee\nEnter[3] to update address of a employee\nEnter[4] to update city of a employee\n"))
        if (v == 1):
            new_no = int(input("Enter employee no whose age u want to update"))
            new = int(input("Enter new age :"))
            c.execute('UPDATE prsnltable3 set AGE=? where EMP_NO=?', (new, new_no))
        elif (v == 2):
            new_no = int(input("Enter employee no whose mobile_no u want to update"))
            new = int(input("Enter new mobile no of a employee:"))
            c.execute('UPDATE prsnltable3 set MOBILE_NO=? where EMP_NO=?', (new, new_no))
        elif (v == 3):
            new_no = int(input("Enter employee no whose address u want to update"))
            new = input("Enter new address :")
            c.execute('UPDATE prsnltable3 set ADDRESS=? where EMP_NO=?', (new, new_no))
        elif (v == 4):
            new_no = int(input("Enter employee no whose city u want to update"))
            new = input("Enter new city :")
            c.execute('UPDATE prsnltable3 set CITY=? where EMP_NO=?', (new, new_no))
        else:
            print("U have entered wrong choice!!")
    else:
        print("U have entered wrong choice!!")


def delete_prsnltable():
    id = int(input("Enter employee no. whose data u want to delete"))
    c.execute('DELETE from prsnltable3 where EMP_NO=?', (id,))


create_profsnltable()
create_prsnltable()
ch = 'y'
while (ch == 'y' or ch == 'Y'):
    try:
        print(
            "\t\t\t\tMAIN MENU\n\t\t\t Enter[1] for professional employee table\n\t\t\t Enter[2] for personal employee table \n\t\t\t Enter[3] for view all details of employee")
        a = int(input("\t\t\tEnter ur choice:"))
        if (a == 1):
            print(
                "\t\tMenu\n Enter[1] to insert data \n Enter[2] to update data\n Enter[3] to view data \n Enter[4] to delete data \n")
            m = int(input("Enter ur choice:"))
            if (m == 1):
                n = int(input("Enter no. of employees whose data u want to insert into database"))
                if n >= 1:
                    for i in range(n):
                        print("Enter data of employee\n")
                        profsnldata_entry()
                else:
                    print("u have entered wrong value")
            elif (m == 2):
                updateprofsnl()
            elif (m == 3):
                select_profsnltable()
            elif (m == 4):
                delete_profsnltable()
            else:
                print("OOPS! u have entered wrong choice")
        elif (a == 2):
            print(
                "\t\t Menu\n Enter[1] to insert data \n Enter[2] to update data\n Enter[3] to view data \n Enter[4] to delete data \n")
            m = int(input("Enter  ur choice:"))
            if (m == 1):
                n = int(input("Enter total no. of employees u want to insert the data"))
                if n >= 1:
                    for i in range(n):
                        print("Enter data of employee\n")
                        insert_prsnltable()
                    else:
                        print("\n Insertion of data is completely succefully")
                else:
                    print("\n u have entered wrong no.")
            elif (m == 2):
                update_prsnltable()
            elif (m == 3):
                select_prsnltable()
            elif (m == 4):
                delete_prsnltable()
            else:
                print("OOPS! u have entered wrong choice")
        elif (a == 3):
            c.execute(
                'SELECT profsnltable2.*,prsnltable3.* from profsnltable2 LEFT OUTER JOIN prsnltable3 on ( profsnltable2.EMP_NO = prsnltable3.EMP_NO )')
            for i in c.fetchall():
                print(i)
        else:
            print("OOPS! u have entered wrong choice")
    except ValueError:
        print("Insert wrong value into table")
    except:
        print("ERROR!!")
    finally:
        ch = input("U want to continue(y/n):")
conn.commit()
c.close()
conn.close()


