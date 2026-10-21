import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="Root",database="DjangoORM")
cur=conn.cursor()
print("Connection created")
# cur.execute("create database DjangoORM")
# print("Database created")


# cur.execute('''create table employee(id int primary key auto_increment,
#     name varchar(30),
#     designation varchar(30),
#     salary decimal(10,2))
# ''')
# print("table created")
# Object-Relational Mapping






class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=','
                placeholder+=','
            cols+=col
            placeholder+='%s'
        values=tuple(kwargs.values())
        # print(f"insert into employee ({cols}) values ({placeholder}),{values}")
        query=f"insert into employee ({cols}) values ({placeholder})"
        cur.execute(query,values)
        print("Data inserted")
        conn.commit()
            

    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())
        
    
    def update(self, *args, **kwargs):
        print(args,kwargs)
        for key in kwargs:               
            cur.execute(f"update employee set {key}='{kwargs.get(key)}'where id ={args[0]}")
            conn.commit()

        print("Updated successfully")


    def delete(self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
        conn.commit()
        print("Deleted successfully")

    
    def filter(self, *args, **kwargs):
        for key in kwargs:
            cur.execute(
                f"select * from employee where {key}=%s",
                (kwargs.get(key),)
            )
            print(cur.fetchall())



employee=Employee()

while True:
    print("1.Create employee")
    print("2.List all employees")
    print("3.Employee detail view")
    print("4.Update employee")
    print("5.Delete employee")
    print("6.Filter employee")
    print("7.Exit")

    choice=int(input("Enter the choice:"))
    if choice==1:
        name=input("Enter the employee name:")
        desig=input("Enter the designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=desig,salary=salary)

    elif choice==2:
        employee.list()

    elif choice==3:
        print("")
        id=int(input("Enter the employee ID:"))
        employee.retrieve(id=id)

    elif choice==4:
        
        id=int(input("Enter the employee id:"))
        print("Update:")
        print("1.Name")
        print("2.Designation")
        print("3.Salary")
        choice=int(input("Enter the choice:"))
        if choice==1:
            name=input("Enter the name:")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("Enter the designation:")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("enter the salary:"))
            employee.update(id,salary=salary)
        else:
            print("Invalid choice")

    elif choice==5:
        id = int(input("Enter the employee ID to delete:"))
        employee.delete(id)


    elif choice==6:
        print("Filter option:")
        print("1.Filter by Name")
        print("2.Filter by Designation")
        print("3.Filter by Salary")
        choice=int(input("Enter the choice:"))
        if choice==1:
            name=input("Enter the name:")
            employee.filter(name=name)
        elif choice==2:
            desig=input("Enter the designation:")
            employee.filter(designation=desig)
        elif choice==3:
            salary=float(input("enter the salary:"))
            employee.filter(salary=salary)
                   
       
    elif choice==7:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
        












conn.close()
print("connection closed")
