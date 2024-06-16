from MyMod import *
import datetime
import sys
import mysql.connector
import random
import string

#Creating a hotel management system
print("____Welcome To XYZ Restaurant____\n".center(50))

login=input("Enter your Login ID:")
for i in login:
     if login=="COOK":
        print("____COOK:XYZ Restaurant____\n".center(50))

#Cook Interface:
        db_name="XYZ"
        connection=mysql.connector.connect(host="localhost",user="root",password="Sonu@07219",database=db_name)
        cur=connection.cursor()
        print("____Welcome Cook____".center(50))
#Display the operations:
        
        while True:
            
          print("\nCOMMANDS:\n")
          print("1.Display the menu\n2.Create a New Menu\n3.Alter the Existing Menu\n4.Drop the Menu\n5.Display structure of Menu\n6.Manipulate Data in the Menu\n7.Display all existing menu\n8.Exit The Interface")
          try:
                ch=int(input("\nPress the Key:"))

                if ch==1:
                     print()
                     DisplayTable(db_name,cur)
                     connection.commit()
                if ch==2:
                    print()
                    createTable(db_name,cur)
                    connection.commit()
                elif ch==3:
                    print()
                   # showTables(db_name,cur)
                    #connection.commit()
                    #tname=input("Enter table Name:")
                    print("\nA:Add new column\nB:Modify existing column\nC:Delete existing column\nD:Exit")
                    ch=input("\nPress the key:")
                    for ch in ch: 
                         if ch=="A":
                                   AddColumn(db_name,cur)
                                   connection.commit()
                         elif ch=="B":
                                   UpdColumn(db_name,cur)
                                   connection.commit()
                         elif ch=="C":
                                   DelColumn(db_name,cur)
                                   connection.commit()
                         elif ch=="D":
                                   break
                         else:
                                   print("Pressed Key-Invalid")
                                   
                elif ch==4:
                     print()
                     DropTable(db_name,cur)
                     connection.commit()
                elif ch==5:
                     print()
                     showTables(db_name,cur)
                     tname=input("Enter table Name:")
                     Desc(db_name,tname,cur)
                     connection.commit()
                elif ch==6:
                    print("\nA.Insert item/s in the Menu\nB.Update item/s in the menu\nC.Delete Item/s from the menu\n".center(50))
                    print()
                    op=input("Press the key for desired operation:")
                    if op=='A':
                              showTables(db_name,cur)
                              tname=input("Enter table Name:")
                              print("The Structure of ",tname)
                              Desc(db_name,tname,cur)
                              print("\n Existing Data:")
                              query="Select * from %s"%(tname,)
                              cur.execute(query)
                              val=cur.fetchall()
                              print(tabulate(val,headers=["Item_ID","Item_Name","Item_Cost"],tablefmt="fancy_grid"))
                     
                              ent=int(input("Enter the Number of entries:"))
                              for i in range(ent):
                                    it_id=input("Enter the Item ID:")
                                    it_name=input("Enter the Item Name:")
                                    it_price=int(input("Enter the Price:"))
                                    query="insert into %s values('%s','%s',%s)"%(tname,it_id,it_name,it_price)
                                    cur.execute(query)
                                    connection.commit()
                                    print(i+1,"  Entry added successfully")
                                    print()

                              print("Insertion into ",tname," done successfully !!!!")
                    elif op=='B':
                              DisplayTable(db_name,cur)
                              #print("Existing Data:\n")
                              tname=input("Re-enter the table name:")
                              rep=int(input("Enter the no. of entries to make change:"))
                              for i in range(0,rep):
                                    it_id=input("Enter the Item_ID:")
                                    rname=input("Enter the row name where change is to be made:")
                                    new_ent=input("Enter the new value:")
                                    cur.execute("UPDATE %s SET %s=%s WHERE Item_ID='%s' "%(tname,rname,new_ent,it_id))
                                    print("Entry Updated successfully")


                    elif op=='C':
                              DisplayTable(db_name,cur)
                              tname=input("Re-enter the table name:")
                              print("1.Delete complete data\n2.Delete a set of data\n")
                              ch=int(input("Press the Key:"))
                              
                              if ch==1:
                                   cur.execute("delete from %s"%(tname,))
                                   print("Complete data deleted from ",(tname.upper()))
                              elif ch==2:
                                   rep=int(input("Enter the no. of entries to make change:"))
                                   for i in range(0,rep):
                                     it_id=input("Enter the Item_Id:")
                                     cur.execute("delete from %s where Item_ID='%s'"%(tname,it_id))
                                     print("\nData deleted where Item_Id=",it_id)
                              else:
                                   print("User Input Error")

                    else:
                                   print("User Input Error")              

                elif ch==7:
                     print()
                     showTables(db_name,cur)
                elif ch>=9 or ch<=0:
                     print("Error:User Input Error")

                elif ch==8:
                     print("THANK YOU !!!!".center(50))                                                                        #variable=datetime.datetime.now()
                     sys.exit()                                                                                                         #nv=variable.strftime("%D-%M-%Y %H:%M")
                                                                                                                               #print(nv)

                     
          except Exception as e:
                              print("Error:",e)
          
     elif login=="CUSTOMER":
          print("!!!!Hello Customer!!!!".center(50))
          print("Welcome to  XYZ  TakeAway".center(50))
          db_name="xyz"
          connection=mysql.connector.connect(host="localhost",user="root",password="Sonu@07219",database="xyz_customer")
          cur=connection.cursor()
          cust_id=''.join(random.choices(string.ascii_letters, k=7))
          while True:
               try:
                   print("\n1.Display The Menu\n2.Order Food from the Menu\n3.Review and Rate\n4.Exit")
                   print()
                   ch=int(input("Press the key:"))
                   if ch==1:
                         showTables(db_name,cur)
                         inp=int(input("Enter the no. of menu to be displayed:"))
                         for i in range(inp):
                                   DisplayTable(db_name,cur)
                                   connection.commit()
                              
                     
                   
                   elif ch==2:
                              DisplayTable(db_name,cur)
                              print("\nA.Order\nB.Exit\n")
                              key=input("Press the Key:")
                              if key=="A":
                                   tname=input("Re-Enter the Menu Name:")
                                   L=[]
                                   while True:
                                         it_id=input("\nEnter the Item_ID(-1 To EXIT):")
                                         if it_id!="-1":
                                            cur.execute("select * from xyz.%s where Item_Id='%s'"%(tname,it_id))
                                            data=cur.fetchall()
                                            for i in data:
                                                     print(i)
                                         #cur.execute("use %s"%(db,))
                                            cur.execute("insert into xyz_customer.order_details (Item_ID,Item_Name,Item_Price) select Item_ID,Item_Name,Item_Price from xyz.%s where Item_ID='%s' "%(tname,it_id))
                                            L.append(it_id)
                                         else:
                                            break
                                   date=datetime.datetime.now()
                                   d=date.strftime("%d-%m-%y %H:%M")
                                   print("\nYour Orders:\n")
                                   orders=""
                                   for i in L:
                                        cur.execute("select Item_Name,Item_Price from xyz.%s where Item_ID='%s' "%(tname,i))
                                        ord=cur.fetchall()
                                        orders+=str(ord)
                                        print(tabulate(ord,tablefmt="fancy_grid"))
                                        cur.execute("Insert into xyz_customer.Total(Item_Price) select Item_Price from xyz.%s where Item_ID='%s'"%(tname,i))
                                   cur.execute("select sum(Item_Price) from xyz_customer.Total")
                                   s = cur.fetchone()[0]  # Accessing the first element of the tuple
                                   total_amount = int(s)
                                   print("Total Amount:$", total_amount)
                                   print()
                                   name=input("Enter your Name:")
                                   ph=int(input("Enter phone number:"))
                                   add=input("Address:")
                                   while True:
                                       print("\nPayment Mode:\n1.Credit Card\n2.Cash\n3.UPI")
                                       pay_mode=int(input("\nselect Mode:"))
                                       if pay_mode==1:
                                          cd_num=input("\nEnter Card Number:")
                                          if len(cd_num)==12:
                                              pm="Credit_card"
                                              cur.execute("Insert into xyz_customer.customer_details(Cust_ID,Cust_Name,Phone_No,Address,Total_Amount,Pay_Mode,Add_Details)values('%s','%s',%s,'%s',%s,'%s','%s')"%(cust_id,name,ph,add,total_amount,pm,cd_num))
                                              print("PAYMENT STATUS:SUCCESS".center(50))
                                              break
                                          else:
                                              print("Card number is Invalid")
                                       elif pay_mode==3:
                                            upi_id=input("\nEnter UPI ID:")
                                            if "@" in upi_id:
                                                pm="UPI"
                                                cur.execute("Insert into xyz_customer.customer_details(Cust_ID,Cust_Name,Phone_No,Address,Total_Amount,Pay_Mode,Add_Details)values('%s','%s',%s,'%s',%s,'%s','%s')"%(cust_id,name,ph,add,total_amount,pm,upi_id))
                                                print("PAYMENT STATUS:SUCCESS\nTHANK YOU !!!".center(50))
                                                break
                                            else:
                                                print("UPI-ID Mismatched")
                                       elif pay_mode==2:
                                            pm="Cash"
                                            cur.execute("Insert into xyz_customer.customer_details(Cust_ID,Cust_Name,Phone_No,Address,Total_Amount,Pay_Mode,Add_Details)values('%s','%s',%s,'%s',%s,'%s','%s')"%(cust_id,name,ph,add,total_amount,pm,"-"))
                                            print("PAYMENT STATUS:SUCCESS\nTHANK YOU !!!".center(50))
                                            break
                                       else:
                                            print("Pressed Key staus:Invalid")
                                            break
                                   cur.execute("Truncate table xyz_customer.Total")
                                   print("___BILL:XYZ RESTAURANT___".center(100))
                                   print("_ "*50,"\n")
                                   print("| "," "*40,"XYZ RESTAURANT"," "*39,"|")
                                   print("_ "*50,"\n")
                                   print("| "," "*35,"FOOD THAT FEELS LIKE HOME"," "*33,"|")
                                   print("_ "*50,"\n")
                                   print("Customer ID"," "*35,"| ",cust_id)
                                   print("_ "*50,"\n")
                                   print("Customer Name"," "*33,"| ",name)
                                   print("_ "*50,"\n")
                                   print("Contact Number"," "*32,"| ",ph)
                                   print("_ "*50,"\n")
                                   print("Address"," "*39,"| ",add)
                                   print("_ "*50,"\n")
                                   print("Orders"," "*40,"| ",orders)
                                   print("_ "*50,"\n")
                                   print("Total Amount"," "*34,"| $",total_amount)
                                   print("_ "*50,"\n")
                                   print("Payment Mode"," "*34,"| ",pay_mode)
                                   print("_ "*50,"\n")
                                   cur.execute("insert into xyz_customer.customer_details(Cust_ID,Cust_Name,Phone_No,Address,Total_Amount,Pay_Mode)values('%s','%s',%s,'%s',%s,%s)"%(cust_id,name,ph,add,total_amount,pay_mode))
                                   connection.commit()
                                   sys.exit()
                                   
                              elif key=="B":
                                   break

                   elif ch==3:
                                   rev=input("Write the Review:\n")
                                   rate=int(input("Rate it out of 5:"))
                                   cur.execute("Insert into xyz_customer.Feedback(Cust_ID,Review,Rating) values('%s','%s','%s')"%(cust_id,rev,rate))
                                   print("THANK YOU FOR YOUR VALUABLE FEEDBACK".center(50))
                                   connection.commit()
                   elif ch==4:
                        sys.exit()
                    
                   else:
                        print("Pressed key-Invalid")

                    


               except Exception as e:
                        print("Error:",e)                    


     elif login=="MANAGER":
          print("MANAGER|XYZ RESTAURANT".center(50))
          db_name="xyz_customer"
          connection=mysql.connector.connect(host="localhost",user="root",password="Sonu@07219",database=db_name)
          cur=connection.cursor()
          while True:
               print("\n1.Staff Overview\n2.Menu Details\n3.Order Information\n4.Feedback Details")
               ch=int(input("Press the key:"))
               try:
                    if(ch==1):
                         print()
                         print("\n Existing Data:")
                         query="Select * from staff_details"
                         cur.execute(query)
                         val=cur.fetchall()
                         print(tabulate(val,headers=["Staff_ID","Name","Designation","Basic_Salary","PF_Deduction","Gross_salary"],tablefmt="fancy_grid"))
                         print("\nA.Insert detail/s of the staff\nB.Update details/s of the staff\nC.Delete detail/s of the staff\nD.Exit".center(50))
                         c=input("Press Key:")
                         if c=="A":
                              ent=int(input("Enter the Number of entries:"))
                              for i in range(ent):
                                    print()
                                    st_id=input("Staff ID:")
                                    st_name=input("Name:")
                                    st_desig=input("Designation:")
                                    st_sal=int(input("Basic Salary:"))
                                    st_pf=0.25*st_sal
                                    st_gsal=st_sal - st_pf
                                    cur.execute("insert into staff_details values('%s','%s','%s',%s,%s,%s)"%(st_id,st_name,st_desig,st_sal,st_pf,st_gsal))
                                    connection.commit()
                                    print(i+1," Entry added successfully")
                                    print("_______________________________")
                         if c=="B":
                              data=cur.execute("select * from staff_details")
                              L=cur.fetchall()
                              emp_id=input("Enter the Employee ID:")
                              for i in L:
                                  for j in L:
                                       print(i,j)
                                       cname=input("Enter the column name where change is to be made:")
                                       new_dat=input("enter the new data:")
                                       cur.execute(" update staff_details set %s=%s where Staff_ID=%s"%(cname,new_dat,emp_id))
                                       print("Modified successfully".center(50))
                                       break
                         else:
                            continue
                              
                              
               except Exception as e:
                    print(e)



                                   
                                                                                      



                         
               

