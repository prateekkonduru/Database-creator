import sqlite3

def table():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

flag = 1
while flag == 1:
    q = int(input("Press \n 1 to insert \n 2 to display \n 3 to delete \n 4 to update \n 5 to End program\n Enter your option here:  "))
    if q==1:
        n = int(input("Enter the number of items u want to insert: "))
        i=0
        while i<n:
            item1 = input("Enter your item here: ")
            quantity1= input("Enter the quantity here: ")
            price1 = input("Enter your price here: ")
            insert(item1,quantity1,price1)
            i=i+1
    elif q==2:
        print(view())
    elif q==3:
        item1 = input("Enter the item to be deleted: ")
        delete(item1)
    elif q==4:
        item1 = input("Enter your item here: ")
        quantity1= input("Enter the quantity here: ")
        price1 = input("Enter your price here: ")
        update(item1,quantity1,price1)
    elif q==5:
        break
    else:
        flag = 0
