from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3 as db


def connection():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()
    sql = '''
    create table if not exists sellings (
        date string,
        product string,
        price number,
        quantity number,
        total number
        )
    '''
    cur.execute(sql)
    connectObj.commit()


connection()
window = Tk()
window.title("Shop Sales and Stock Managing")
tabs = ttk.Notebook(window)
root = ttk.Frame(tabs)
root2 = ttk.Frame(tabs)

tabs.add(root, text='Sell')
tabs.add(root2, text='Stock')
tabs.pack(expand=1, fill="both")


# -----------------------------------tab1 ----------------------------------

def GenerateBill():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()

    global billarea
    if p1quantity.get() == 0 and p2quantity.get() == 0 and p3quantity.get() == 0 and p4quantity.get() == 0:
        messagebox.showerror("Error", "No product purchased")
    else:
        billarea.delete('1.0', END)
        billarea.insert(END, "\t|| Shop Sales and Stock Managing ||")
        billarea.insert(END, "\n_______________\n")
        billarea.insert(END, "\nDate\t Products\tPrice\t   QTY\t Total")
        billarea.insert(END, "\n==========================================")

        price = IntVar()
        price2 = IntVar()
        price3 = IntVar()
        price4 = IntVar()

        print(dateE.get())
        price = price2 = price3 = price4 = 0

        if p1quantity.get() != 0:
            price = p1quantity.get() * p1price.get()
            print(price)
            billarea.insert(END, f"\n{dateE.get()}\t {p1name.get()} \t{p1price.get()}\t {p1quantity.get()}\t {price}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), p1name.get(), p1price.get(), p1quantity.get(), price))
            connectObj.commit()

        if p2quantity.get() != 0:
            price2 = (p2quantity.get() * p2price.get())
            print(price2)
            billarea.insert(END, f"\n{dateE.get()}\t {p2name.get()} \t{p2price.get()}\t {p2quantity.get()}\t {price2}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            print(dateE.get(), 'Product-2', p2price.get(), p2quantity.get(), price2)
            cur.execute(sql, (dateE.get(), p2name.get(), p2price.get(), p2quantity.get(), price2))
            connectObj.commit()

        if p3quantity.get() != 0:
            price3 = p3quantity.get() * p1price.get()
            print(price3)
            billarea.insert(END, f"\n{dateE.get()}\t{p3name.get()}\t{p3price.get()}\t {p3quantity.get()}\t {price3}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), p1name.get(), p3price.get(), p3quantity.get(), price3))
            connectObj.commit()

        if p4quantity.get() != 0:
            price4 = p4quantity.get() * p1price.get()
            billarea.insert(END, f"\n{dateE.get()}\t{p4name.get()}\t{p4price.get()}\t {p4quantity.get()}\t {price4}")

            sql = '''
            INSERT INTO Sellings VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), p4name.get(), p4price.get(), p4quantity.get(), price4))
            connectObj.commit()

        Totalprice = IntVar()
        Totalprice = price + price2 + price3 + price4

        Totalquantity = IntVar()
        Totalquantity = p1quantity.get() + p2quantity.get() + p3quantity.get() + p4quantity.get()
        billarea.insert(END, f"\nTotal \t \t  \t{Totalquantity}\t {Totalprice}")


def view():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()

    sql = 'Select * from Sellings'
    cur.execute(sql)

    rows = cur.fetchall()
    viewarea.insert(END, f"Date\t Product\t  Price of 1\t  Quantity\t  Price\n")

    for i in rows:
        allrows = ""
        for j in i:
            allrows += str(j) + '\t'
        allrows += '\n'
        viewarea.insert(END, allrows)


dateL = Label(root, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE = DateEntry(root, width=12, font=('arial', 15, 'bold'))
dateE.grid(row=0, column=1, padx=7, pady=7)

l = Label(root, text="Product", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root, text="Price", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=1, padx=7, pady=7)

l = Label(root, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=2, padx=7, pady=7)

# ----product 1----------------------------------------------------
p1name = StringVar()
p1name.set('Product1')

p1price = IntVar()
p1price.set(100)

p1quantity = IntVar()
p1quantity.set(0)

l = Entry(root, text=p1name, font=('arial', 15, 'bold'), width=12)
l.grid(row=2, column=0, padx=7, pady=7)

l = Entry(root, text=p1price, font=('arial', 15, 'bold'), width=12)
l.grid(row=2, column=1, padx=7, pady=7)

t = Entry(root, textvariable=p1quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=2, column=2, padx=7, pady=7)

# ----product 2-------------------------------------------------------------
p2name = StringVar()
p2name.set('Product2')

p2price = IntVar()
p2price.set(200)

p2quantity = IntVar()
p2quantity.set(0)

l = Entry(root, text=p2name, font=('arial', 15, 'bold'), width=12)
l.grid(row=3, column=0, padx=7, pady=7)

l = Entry(root, text=p2price, font=('arial', 15, 'bold'), width=12)
l.grid(row=3, column=1, padx=7, pady=7)

t = Entry(root, textvariable=p2quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=3, column=2, padx=7, pady=7)

# ----product 3----
p3name = StringVar()
p3name.set('Product3')

p3price = IntVar()
p3price.set(300)

p3quantity = IntVar()
p3quantity.set(0)

l = Entry(root, text=p3name, font=('arial', 15, 'bold'), width=12)
l.grid(row=4, column=0, padx=7, pady=7)

l = Entry(root, text=p3price, font=('arial', 15, 'bold'), width=12)
l.grid(row=4, column=1, padx=7, pady=7)

t = Entry(root, textvariable=p3quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=4, column=2, padx=7, pady=7)

# ----product 4----
p4name = StringVar()
p4name.set('Product4')

p4price = IntVar()
p4price.set(400)

p4quantity = IntVar()
p4quantity.set(0)

l = Entry(root, text=p4name, font=('arial', 15, 'bold'), width=12)
l.grid(row=5, column=0, padx=7, pady=7)

l = Entry(root, text=p4price, font=('arial', 15, 'bold'), width=12)
l.grid(row=5, column=1, padx=7, pady=7)

t = Entry(root, textvariable=p4quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=5, column=2, padx=7, pady=7)

# ------------------------bill-------------------------
billarea = Text(root)

submitbtn = Button(root, command=GenerateBill, text="Bill",
                   font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

submitbtn.grid(row=6, column=0, padx=7, pady=7)

viewbtn = Button(root, command=view, text="View All Sellings",
                 font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

viewbtn.grid(row=6, column=2, padx=7, pady=7)

billarea.grid(row=9, column=0)
viewarea = Text(root)
viewarea.grid(row=9, column=2)


# ----------------------------------------------tab2 ----------------------------------
def connection2():
    connectObj2 = db.connect("shopManagement.db")
    cur = connectObj2.cursor()
    sql = '''
    create table if not exists stocks (
        date string,
        product string,
        price number,
        quantity number
        )
    '''
    cur.execute(sql)
    connectObj2.commit()


connection2()


def addStock():
    global dateE2, qty, name, price

    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()
    sql = '''
            INSERT INTO stocks VALUES 
            (?, ?, ?, ?)
            '''
    cur.execute(sql, (dateE2.get(), name.get(), price.get(), qty.get()))
    connectObj.commit()


def viewStock():
    connectObj = db.connect("shopManagement.db")
    cur = connectObj.cursor()

    sql = 'Select * from stocks'
    cur.execute(sql)

    rows = cur.fetchall()
    viewarea2.insert(END, f"Date \tProduct\t  Price\t  Quantity\t \n")

    for i in rows:
        allrows = ""
        for j in i:
            allrows += str(j) + '\t'
        allrows += '\n'
        viewarea2.insert(END, allrows)


dateL = Label(root2, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE2 = DateEntry(root2, width=12, font=('arial', 15, 'bold'))
dateE2.grid(row=0, column=1, padx=7, pady=7)

l = Label(root2, text="Product", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root2, text="Price", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=2, column=0, padx=7, pady=7)

l = Label(root2, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=3, column=0, padx=7, pady=7)

name = StringVar()
price = IntVar()
qty = IntVar()

Name = Entry(root2, textvariable=name, font=('arial', 15, 'bold'), width=12)
Name.grid(row=1, column=1, padx=7, pady=7)

Price = Entry(root2, textvariable=price, font=('arial', 15, 'bold'), width=12)
Price.grid(row=2, column=1, padx=7, pady=7)

Qty = Entry(root2, textvariable=qty, font=('arial', 15, 'bold'), width=12)
Qty.grid(row=3, column=1, padx=7, pady=7)

addbtn = Button(root2, command=addStock, text="Add",
                font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

addbtn.grid(row=4, column=1, padx=7, pady=7)

viewarea2 = Text(root2)
viewarea2.grid(row=5, column=0, columnspan=2)

viewbtn2 = Button(root2, command=viewStock, text="View Stock",
                  font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

viewbtn2.grid(row=4, column=0, padx=7, pady=7)

mainloop()