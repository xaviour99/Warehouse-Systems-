from tkinter import *
from tkinter import messagebox as ms
import mysql.connector as mc
from tkinter import ttk

def chkloginu():
    
    
    win2 = Toplevel(win1)
    
    win2.title("Admin login")
    win2.geometry("300x300")
   
    L1 = Label(win2, text='USERNAME')
    L1.grid(row=0, column=0)
    userentry1 = Entry(win2, width=10, textvariable=user)
    userentry1.grid(row=0, column=1)
            
    l2 = Label(win2, text='PASSWORD')
    l2.grid(row=1, column=0)
    passwordentry1 = Entry(win2, width=10, textvariable=password, show="*")
    passwordentry1.grid(row=1, column=1)
            
    b3 = Button(win2, text="Login", command=chklogin)
    b3.grid(row=2, column=1)
            
    b4 = Button(win2, text="Quit", command=win2.destroy)
    b4.grid(row=2, column=2)

     

def chkloginc():
    
    win3=Toplevel(win1)
    win3.title("Customer login")
    win3.geometry("300x300")
    
    L3 = Label(win3, text='USERNAME')
    L3.grid(row=0, column=0)
    userentry = Entry(win3, width=10, textvariable=user1)
    userentry.grid(row=0, column=1)
        
    l4 = Label(win3, text='PASSWORD')
    l4.grid(row=1, column=0)
    passwordentry = Entry(win3, width=10, textvariable=password1, show="*")
    passwordentry.grid(row=1, column=1)
        
    b5 = Button(win3, text="Login", command=chklogin1)
    b5.grid(row=2, column=1)
        
    b6 = Button(win3, text="Quit", command=win3.destroy)
    b6.grid(row=2, column=2)

    b7 = Button(win3, text="Create a customer account" , command=crtcut)
    b7.grid(row=3, column=2)

def chklogin():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("select * from empl where ename='%s' and passwd ='%s'"%(user.get(),password.get()))
    rows=cur.fetchall()
    conn.commit()
    print(len(rows))
    
    if (user.get() == "a" and password.get() == "1"):
        ms.showinfo("Successful", "You are successfully logged in")
        admineditmode()
        
    elif(len(rows)==1):
        
        ms.showinfo("Successful", "You are successfully logged in")
        admineditmode()
        
    else:
        chkfault()
        win2.destroy() 
        

def chklogin1():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("select * from cust where cname='%s' and passwd  ='%s'"%(user1.get(),password1.get()))
    rows=cur.fetchall()
    conn.commit()
    print(len(rows))
   
    
    if (user1.get() == "b" and password1.get() == "2"):
        ms.showinfo("Successful", "You are successfully logged in")
        plorder()
        
    elif(len(rows)==1):
        
        ms.showinfo("Successful", "You are successfully logged in")
        plorder()
      
   
    else:
        chkfault()
        win3.destroy() 



def chkfault():
    if (user.get() != "a" and password.get() != "1"):
        ms.showerror("Error", "Username and password not matched")
    elif (user1.get() == "b" and password1.get() != "2"):
        ms.showerror("Error", "Password not matched")
    else:
        ms.showerror("Error", "Username not matched")
   
def crtcut():
    win4 = Toplevel(win1)
    
    win4.title("Create customer")
    win4.geometry("300x300")
   
     
    l5 = Label(win4, text="Customer Name")
    l5.grid(row=0, column=0)
    e6 = Entry(win4,textvariable=fullname1)
    e6.grid(row=0, column=6)
    
    l6 = Label(win4, text="Address")
    l6.grid(row=2, column=0)
    e7 = Entry(win4,textvariable=address1)
    e7.grid(row=2, column=6)
    
    l7 = Label(win4, text="Phone")
    l7.grid(row=4, column=0)
    e8 = Entry(win4,textvariable=number1)
    e8.grid(row=4, column=6)

    l8 = Label(win4, text="Password")
    l8.grid(row=6, column=0)
    e9 = Entry(win4,textvariable=password1,show="*")
    e9.grid(row=6, column=6)

   
    b8 = Button(win4, text="Sign in", command=crecust)
    b8.grid(row=8, column=6)

def crecust():
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "", 
                              db = "wareh")
    
    cur = conn.cursor()
    cur.execute("insert into cust values(NULL,'%s','%s',%s,'%s',NULL)"%(fullname1.get(),address1.get(),number1.get(),password1.get()))
    conn.commit()
    cur.execute(cur.execute("select c_id from cust where cname='%s' and phone=%s"%(fullname1.get(),number1.get())))
    rows=cur.fetchall()
    
    ms.showinfo("login","user has been successfully generated ,your cust id is {}".format(rows[0][0]))
    
def plorder():
    win5 = Toplevel(win1)
    win5.title("Shipment Name")
    win5.geometry("300x300")

    l9 = Label(win5, text="Shipment Name")
    l9.grid(row=0, column=0)
    e10 = Entry(win5,textvariable=shipname)
    e10.grid(row=0, column=6)
    
    l9 = Label(win5, text="Date")
    l9.grid(row=2, column=0)
    e10 = Entry(win5,textvariable=datecust)
    e10.grid(row=2, column=6)

    l10= Label(win5, text="Quantity")
    l10.grid(row=4, column=0)
    e11 = Entry(win5,textvariable=quantity)
    e11.grid(row=4, column=6)

    l11 = Label(win5, text="P_id")
    l11.grid(row=6, column=0)
    e12 = Entry(win5,textvariable=p_id)
    e12.grid(row=6, column=6)
    
    l33 = Label(win5, text="C_id")
    l33.grid(row=8, column=0)
    e34 = Entry(win5,textvariable=customerid)
    e34.grid(row=8, column=6)
    
    l26 = Label(win5, text="Status")
    l26.grid(row=10, column=0)
    e27 = Entry(win5,textvariable=statship)
    e27.grid(row=10, column=6)

   
    b9 = Button(win5, text="Place order",command=plod)
    b9.grid(row=12, column=6)
def plod():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "", 
                              db = "wareh")
    
    cur = conn.cursor()
    cur.execute("insert into ship values(NULL,'%s','%s','%s','%s','%s','%s',NULL)"%(shipname.get(),datecust.get(),quantity.get(),p_id.get(),customerid.get(),statship.get()))
    conn.commit()
    cur.execute(cur.execute("select SHIP_ID from ship where shipname='%s' and  QUANTITY=%s"%(shipname.get(),quantity.get())))
    rows=cur.fetchall()
    
    ms.showinfo("Place order","your has been successfully places ,your shipment id  is {}".format(rows[0][0]))

def admineditmode():

    win6 = Toplevel(win1)
    win6.title("Choose For The Work")
    win6.geometry("300x300")

    menu1 = Menu(win6)
    menuitem = Menu(menu1,tearoff=0)
    menuitem1 = Menu(menu1,tearoff=0)
    menuitem2 = Menu(menu1,tearoff=0)
    menuitem3 = Menu(menu1,tearoff=0)
    menuitem4 = Menu(menu1,tearoff=0)
    menuitem5 = Menu(menu1,tearoff=0)
    
    menu1.add_cascade(label=" Employee",menu=menuitem)
    menu1.add_cascade(label="Warehouse",menu=menuitem1)
    menu1.add_cascade(label="Order",menu=menuitem2)
    menu1.add_cascade(label="Inventory",menu=menuitem3)
   # menu1.add_cascade(label="Stock",menu=menuitem4)
    menu1.add_cascade(label="Update",menu=menuitem5)
    
    menuitem.add_command(label="Add Employee",command=addemp)
    menuitem.add_command(label="Delete Employee",command=delepm)
    
    menuitem1.add_command(label="Add Warehouse",command=addware)
    menuitem1.add_command(label="Delete Warehouse",command=delware)
    
    menuitem2.add_command(label="Pending Orders",command=pedord)
    menuitem2.add_command(label="Dispached",command=desord)
    
    menuitem3.add_command(label="Check Inventory",command=serinn)
    menuitem3.add_command(label="Add inventory",command=addinve)
    menuitem3.add_command(label="Delete inventory",command=delinve)
    
   # menuitem4.add_command(label="Display Stock")
    menuitem5.add_command(label="Assign Employee for cust",command=assemp)
    menuitem5.add_command(label="Assign Employee for ship",command=shiass)
    
    menuitem5.add_command(label="delcust",command=delcust)

    
    win6.config(menu=menu1)


def delcust():
    win21 = Toplevel(win1)
    win21.title("Delete Customer")
    win21.geometry("300x300")
    
    
    l48 = Label(win21, text='Enter Customer_id')
    l48.grid(row=0, column=0)
    e48 = Entry(win21, width=10, textvariable=customerid)
    e48.grid(row=0, column=1)
    
    b48 = Button(win21, text="Delete",command=delcu)
    b48.grid(row=2, column=6)
    
def delcu():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("delete from cust where c_id=%s"%(customerid.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully deleted")
def assemp():
    win17 = Toplevel(win1)
    win17.title("Assign Employee For Cust")
    win17.geometry("300x300")
    
    l47 = Label(win17, text='E_id')
    l47.grid(row=2, column=0)
    e47 = Entry(win17, width=10, textvariable=e_id)
    e47.grid(row=2, column=1)
    

    
    l33 = Label(win17, text='c_id')
    l33.grid(row=4, column=0)
    e34 = Entry(win17, width=10, textvariable=customerid)
    e34.grid(row=4, column=1)
    

    
    b22 = Button(win17, text="Submit",command=asscust)
    b22.grid(row=6, column=6)
    
def shiass():
    win20 = Toplevel(win1)
    win20.title("Assign Employee For Ship")
    win20.geometry("300x300")
    
    l45 = Label(win20, text='Ship_id')
    l45.grid(row=0, column=0)
    e45 = Entry(win20, width=10, textvariable=shipid)
    e45.grid(row=0, column=1)
    
    l46 = Label(win20, text='E_id')
    l46.grid(row=2, column=0)
    e46 = Entry(win20, width=10, textvariable=e_id)
    e46.grid(row=2, column=1)
    
    b33 = Button(win20, text="Submit",command=shipup)
    b33.grid(row=6, column=6)
def asscust():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("update cust set e_id=%s where c_id=%s "%(e_id.get(),customerid.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully  assign empl ")
def shipup():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("update ship set e_id=%s where ship_id=%s "%(e_id.get(),shipid.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully assign empl in")
    
def addware():
    win14 = Toplevel(win1)
    win14.title("Add Warehouse")
    win14.geometry("300x300")
    
    l12 = Label(win14, text='Warehouse Name')
    l12.grid(row=0, column=0)
    e13 = Entry(win14, width=10, textvariable=wname)
    e13.grid(row=0, column=1)
    
    l13 = Label(win14, text='Address')
    l13.grid(row=2, column=0)
    e14 = Entry(win14, width=10, textvariable=address2)
    e14.grid(row=2, column=1)
    
    
    b10 = Button(win14, text="Submit",command=inware)
    b10.grid(row=4, column=6)

def inware():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("insert into ware1 values(NULL,'%s','%s')"%(wname.get(),address2.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully  added  warehouse")
def delware():
    win16 = Toplevel(win1)
    win16.title("Delete Warehouse ")
    win16.geometry("300x300")
    
    
    l16 = Label(win16, text='Enter Warehouse id')
    l16.grid(row=0, column=0)
    e17 = Entry(win16, width=10, textvariable=w_id)
    e17.grid(row=0, column=1)
    
    b11 = Button(win16, text="Delete",command=reware)
    b11.grid(row=2, column=6)
 
def reware():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("delete from ware1 where w_id=%s"%(w_id.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully dele warehouse")
def addemp():
    win7 = Toplevel(win1)
    win7.title("Add Employee")
    win7.geometry("300x300")
    
    l12 = Label(win7, text='Name')
    l12.grid(row=0, column=0)
    e13 = Entry(win7, width=10, textvariable=fullname)
    e13.grid(row=0, column=1)
    
    l13 = Label(win7, text='Address')
    l13.grid(row=2, column=0)
    e14 = Entry(win7, width=10, textvariable=address)
    e14.grid(row=2, column=1)
    
    l14 = Label(win7, text='Number')
    l14.grid(row=4, column=0)
    e15 = Entry(win7, width=10, textvariable=number)
    e15.grid(row=4, column=1)
    
    l15 = Label(win7, text='Password')
    l15.grid(row=6, column=0)
    e16 = Entry(win7, width=10, textvariable=password,show="*")
    e16.grid(row=6, column=1)
    
    l151 = Label(win7, text='w_id')
    l151.grid(row=8, column=0)
    e161 = Entry(win7, width=10, textvariable=w_id)
    e161.grid(row=8, column=1)
    
    b10 = Button(win7, text="Submit",command=insertemp)
    b10.grid(row=10, column=6)


def insertemp():
    
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("insert into empl values(NULL,'%s','%s',%s,'%s',%s)"%(fullname.get(),address.get(),number.get(),password.get(),w_id.get()))
    conn.commit()
    cur.execute(cur.execute("select e_id from empl where ename='%s' and phone=%s"%(fullname.get(),number.get())))
    rows=cur.fetchall()
    ms.showinfo("Createde","user has been successfully generated ,your empl id is {}".format(rows[0][0]))
def delepm():
    win8 = Toplevel(win1)
    win8.title("Delete Employe")
    win8.geometry("300x300")
    
    
    l16 = Label(win8, text='Enter Empoyloyee_id')
    l16.grid(row=0, column=0)
    e17 = Entry(win8, width=10, textvariable=e_id)
    e17.grid(row=0, column=1)
    
    b11 = Button(win8, text="Delete",command=delemp)
    b11.grid(row=2, column=6)
    
def delemp():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("delete from empl where e_id=%s"%(e_id.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully deleted empl")
    
    
def pedord():
    
     
    win9 = Toplevel(win1)
    win9.title("Pending Orders")
    win9.geometry("700x700")
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute('select * from ship where statu="Pending"')
    data=cur.fetchall()    
    frame = Frame(win9)
    frame.grid(row=0,column=0)

    tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 5, show = "headings")
    tree.grid(row=2,column=0)

    tree.heading(1, text="Ship_id")
    tree.heading(2, text=" sname ")
    tree.heading(3, text="date_of_ship ")
    tree.heading(4, text="quantity")
    tree.heading(5, text=" p_id ")
    tree.heading(6, text=" c_id ")
    tree.heading(7, text=" Status ")
    tree.heading(8, text=" e_id ")
    
    
    
    

    tree.column(1, width = 100)
    tree.column(2, width = 100)
    tree.column(3, width = 100)
    tree.column(4, width = 100)
    tree.column(5, width = 100)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 100)

    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.grid(row=4,column=0)

    tree.configure(yscrollcommand=scroll.set)

    for val in data:
         tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7] ))
    
     

    b12 = Button(win9, text="Dispach",command=des)
    b12.grid(row=12,column=10)
def genrecipt():
    win31 = Toplevel(win1)
    win31.title("Receipt")
    win31.geometry("700x700")
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    
    l60 = Label(win31, text='Date')
    l60.grid(row=0, column=0)
    e60 = Entry(win31, width=10, textvariable=datere)
    e60.grid(row=0, column=2)
    
    l61 = Label(win31, text='Ship_id')
    l61.grid(row=2, column=0)
    e61 = Entry(win31, width=10, textvariable=shipid)
    e61.grid(row=2, column=2)
    
    l63 = Label(win31, text='Total quantity')
    l63.grid(row=4, column=0)
    e63 = Entry(win31, width=10, textvariable=quantity)
    e63.grid(row=4, column=2)
    
    b63 = Button(win31, text="Dispach",command=genre)
    b63.grid(row=12,column=10)
def genre():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("insert into receipt values('%s',%s,'%s')"%(datere.get(),shipid.get(),quantity.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully generated receipt ")
    
    
def des():
    win30 = Toplevel(win1)
    win30.title("Dispatch")
    win30.geometry("700x700")
    
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    
    
    l62 = Label(win30, text='Ship_id')
    l62.grid(row=0, column=0)
    e62 = Entry(win30, width=10, textvariable=shipid)
    e62.grid(row=0, column=2)
    
    
    b62 = Button(win30, text="Ok",command=ships)
    b62.grid(row=2,column=0)
    
    
def ships():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("select quantity,p_id from ship where ship_id=%s"%(shipid.get()))
    qty1=cur.fetchall()
    cur.execute("select quantity from prod where p_id=%s"%(qty1[0][1]))
    qty2=cur.fetchone()
    totqty=qty2[0]-qty1[0][0]
    cur.execute("update prod set quantity=%s where p_id=%s"%(totqty,qty1[0][1]))
    cur.execute("update ship set statu='dispatched' where ship_id=%s"%(shipid.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully dispatched the order generate receipt")
    
def desord():
    
    win10 = Toplevel(win1)
    win10.title("Despatch")
    win10.geometry("700x700")
    
        
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute('select * from ship where Statu="Dispatched"')
    data=cur.fetchall()
    
    frame = Frame(win10)
    frame.grid(row=0,column=0)

    tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 5, show = "headings")
    tree.grid(row=2,column=0)

    tree.heading(1, text="Ship_id")
    tree.heading(2, text="Ship name")
    tree.heading(3, text="date_of_ship ")
    tree.heading(4, text="quantity")
    tree.heading(5, text=" p_id ")
    tree.heading(6, text=" c_id ")
    tree.heading(7, text=" Status ")
    tree.heading(8, text=" e_id ")
    
    
    
    
    

    tree.column(1, width = 100)
    tree.column(2, width = 100)
    tree.column(3, width = 100)
    tree.column(4, width = 100)
    tree.column(5, width = 100)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 100)

    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.grid(row=4,column=0)

    tree.configure(yscrollcommand=scroll.set)

    for val in data:
         tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7] ))
         

    b67 = Button(win10, text="Generate Receipt",command=genrecipt)
    b67.grid(row=12,column=10)
    
    b13 = Button(win10, text="Ok",command=win10.destroy)
    b13.grid(row=10,column=10)


def serinn():
         
    win45 = Toplevel(win1)
    win45.title("Pending Orders")
    win45.geometry("700x700")
    
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute('select * from prod ')
    data=cur.fetchall()    
    frame = Frame(win45)
    frame.grid(row=0,column=0)

    tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 5, show = "headings")
    tree.grid(row=2,column=0)

    tree.heading(1, text="P_id")
    tree.heading(2, text="Pname ")
    tree.heading(3, text=" Date of Manf")
    tree.heading(4, text=" W_id ")
    tree.heading(5, text=" Quantity ")

    
    
    
    

    tree.column(1, width = 100)
    tree.column(2, width = 100)
    tree.column(3, width = 100)
    tree.column(4, width = 100)
    tree.column(5, width = 100)


    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.grid(row=4,column=0)

    tree.configure(yscrollcommand=scroll.set)

    for val in data:
         tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4] ))
    
     

    b12 = Button(win45, text="Ok",command=win45.destroy)
    b12.grid(row=12,column=10)

    
def addinve():
    win12 = Toplevel(win1)
    win12.title("Add Inventory")
    win12.geometry("300x300")
    
    l19 = Label(win12, text='Product Name')
    l19.grid(row=0, column=0)
    e20 = Entry(win12, width=10, textvariable=prodname)
    e20.grid(row=0, column=1)
    
    l20 = Label(win12, text='Date of Manf')
    l20.grid(row=2, column=0)
    e21 = Entry(win12, width=10, textvariable=date)
    e21.grid(row=2, column=1)
    
    l22 = Label(win12, text='Quantity')
    l22.grid(row=4, column=0)
    e23 = Entry(win12, width=10, textvariable=quan)
    e23.grid(row=4, column=1)
    
    l50 = Label(win12, text='warehouse')
    l50.grid(row=6, column=0)
    e50 = Entry(win12, width=10, textvariable=w_id)
    e50.grid(row=6, column=1)
    
    b14 = Button(win12, text="Submit",command=addin)
    b14.grid(row=10, column=6)
def addin():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("insert into prod values(NULL,'%s','%s','%s','%s')" %(prodname.get(),date.get(),quan.get(),w_id.get()))
    conn.commit()
    cur.execute(cur.execute("select p_id from prod where pname='%s' and quantity=%s"%(prodname.get(),quan.get())))
    rows=cur.fetchall()
    ms.showinfo("Inventory Added","Inventory has been successfully Added ,your p_id is {}".format(rows[0][0]))
    
     
def delinve():
    win13 = Toplevel(win1)
    win13.title("Delete Product")
    win13.geometry("300x300")
    
    
    l21 = Label(win13, text='Product id')
    l21.grid(row=0, column=0)
    e22 = Entry(win13, width=10, textvariable=p_id)
    e22.grid(row=0, column=1)
    
    b15 = Button(win13, text="Delete",command=delin)
    b15.grid(row=2, column=6)
    
def delin():
    conn = mc.connect (host = "localhost",
                              user = "root",
                              password = "",
                              db = "wareh")
    cur = conn.cursor()
    cur.execute("delete from prod where p_id=%s"%(p_id.get()))
    conn.commit()
    ms.showinfo("Successful", "You are successfully deleted inventory")
    
    
win1 =Tk()
win1.title("Select Mode")
win1.geometry("300x300")
frame1 = Frame(win1)
frame1.pack()
user = StringVar()
user1 = StringVar()
password = StringVar()
password1 = StringVar()
fullname = StringVar()
fullname1 = StringVar()
address = StringVar()
address1 = StringVar()
address2=StringVar()
number = StringVar()
number1 =StringVar()
productname = StringVar()
quantity = StringVar()
qty=0

location = StringVar()
employeeid = StringVar()
customerid = StringVar()
e_id=StringVar()
prodname=StringVar()
quan=StringVar()
p_id=StringVar()
pname=StringVar()
date=StringVar()
serch=StringVar()
wname=StringVar()
shipid=StringVar()
w_id=StringVar()
shipname=StringVar()
datecust=StringVar()
datere=StringVar()
statship=StringVar()
rep_id = StringVar()

b1 = Button(frame1, text="Admin", command=chkloginu )
b1.grid(row=200, column=1)

b2 = Button(frame1, text="Customer", command=chkloginc)
b2.grid(row=200, column=2)

