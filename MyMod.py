#print("MySQL Functions")
import mysql.connector
from tabulate import tabulate
from prettytable import PrettyTable
import sys
# create a database
def create(db,c):
    query="create database if not  exists %s "%(db,)
    c.execute(query)
    print("____Created/Entered Successfully____".center(50))
        
# drop a database
def drop(db,c):
    query="drop database if  exists %s "%(db,)
    c.execute(query)
    print("Database dropped successfully")


# create a table in database

def createTable(db,c):
    c.execute(" use %s "%(db,))
    tname=input("Enter new table name:")
    ch=int(input("Enter the Number of Rows:"))
    for i in range(ch):
           if i==0:
              name=input("Enter The Row Name (entry must be unique):")
              dt=input("Enter datatype:")
              size=int(input("Enter the size:"))
              query="create table if not exists %s( %s %s (%s) primary key)" %(tname,name,dt,size)   
              c.execute(query)

           else:
              name=input("Enter The Row Name :")
              dt=input("Enter datatype:")
              size=int(input("Enter the size:"))
              query="alter table %s add( %s %s (%s) not null)" %(tname,name,dt,size)   
              c.execute(query)
   #c.execute("Create table )
    print("Table Created successfully")
    Desc(db,tname,c)
    
    
# Drop a table
def DropTable(db,c):
    create(db,c)
    c.execute(" use %s "%(db,))
    print("\nEntered the database")
    showTables(db,c)
    tname=input("Enter table name:")
    c.execute("show tables")
    t=c.fetchall()
    for i in t:
       if tname in t:
           print(" ".center(25),tname," table dropped successfully")
           break
       elif tname not in t:
          c.execute("drop table %s"%(tname,))
          print(" ".center(25),tname," table doesn't exist")


#BluePrint of the table
def Desc(db,tb,c):
    c.execute("use %s"%(db,))
    c.execute("Desc %s" %(tb,))
    data=c.fetchall()
    t=PrettyTable(["Row_name","DataType","Add-ON1","Add-ON2","Add-ON3","Add-On4"])
    for i in data:
        t.add_row(i)
    print(t)
    
    #print("\nTable Constraints:")
    #print(tabulate(data,tablefmt="fancy_grid"))





# Print the data

def show(db,c):
    create(db,c)
    c.execute(" use %s "%(db,))
    print("Entered the database")
    tb=input("Enter table name:")
    Desc(db,tb,c)
    c.execute("Select * from %s "%(tb,))
    data=c.fetchall()
    rcount=int(input("Enter the number of rows in the table:"))
    a=""
    i=1
    while rcount>0:
        n=input("Enter title for the row ",i,":")
        a=a+" "+n
        i+=1
        rcount-=1
    print(tabulate(data,headers=a.split(),tablefmt="psql"))         #    print(tabulate(data,headers=["c1","c2","c3"],tablefmt="fancy_grid"))



# Display the menu(Only for Hotel Management System):
def DisplayTable(db,c):
    c.execute(" use %s "%(db,))
    c.execute("show tables")
    tbs=c.fetchall()
    print("Available Tables:\n")
    print(tabulate(tbs,headers=["Table_Name"],tablefmt="fancy_grid"))
    tb_name=input("Enter table name:")
    for i in range(1):
      try:
          query="Select * from %s"%(tb_name,)
          c.execute(query)
          val=c.fetchall()
          print(tabulate(val,headers=["Item_ID","Item_Name","Item_Price"],tablefmt="fancy_grid"))
      except Exception as e:
          print("Error 404:",e)
          break
         
# Show the tables from the database:
def showTables(db,c):
    c.execute("use %s"%(db,))
    query="show tables"
    c.execute(query)
    tabs=c.fetchall()
    print("Available/Existing Tables:")
    print(tabulate(tabs,headers=['Table_name','Constraints'],tablefmt='psql'))

# More alter functions:
def AddColumn(db,c):
    showTables(db,c)
    tname=input("Enter Table Name:")
    print("--Adding New Column--".center(50))
    name=input("Enter new column name:")
    dt=input("Enter the datatype:")
    sz=int(input("Enter the size:"))
    c.execute("alter table %s add (%s %s (%s) not null)"%(tname,name,dt,sz))
    print("Added successfully")

def DelColumn(db,c):
    showTables(db,c)
    tb=input("Enter Table Name:")
    Desc(db,tb,c)
    print("--Deleting Existing Column--".center(50))
    name=input("Enter column name:")
    c.execute("alter table %s drop column %s"%(tb,name))
    print("Deleted successfully")

def UpdColumn(db,c):

    showTables(db,c)
   # Desc(db,tb,c)
    tb=input("Table Name:")
    Desc(db,tb,c)
    c.execute("desc %s"%(tb,))
    data=c.fetchall()
    l=int(input("Enter the no. of rows from the above table:"))
    rname=input("Enter the Row Name where you want to make change:")
    nd=list(data)
    for i in data:
                for i in range(0,l):
                   for j in range(0,l):
                     if data[i][j]==rname:
                        print("-"*25 ,"Entering new Constraints ","-"*25)
                        newD=input("Enter new datatype:")
                        newS=int(input("Enter the new size:"))
                        c.execute("alter table %s modify %s %s (%s) not null"%(tb,rname,newD,newS))
                        print("\nModified Successfully")
                        break
                     else:
                        continue
                   


