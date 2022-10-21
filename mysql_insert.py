import mysql.connector
mydb=mysql.connector.connect(    
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
book_list=[["Harry Potter","Jk Rowling","August 24th"],
            ["The Hulk","Russo Brothers","July 25th"]]
mycursor=mydb.cursor()
sql="INSERT INTO book(title,author,date) VALUES(%s,%s,%s)"
for book in book_list:
    mycursor.execute(sql,book)
    print(mycursor.rowcount,"record inserted")
mydb.commit()

# mycursor.execute("SELECT * FROM book")
# myresult=mycursor.fetchall()

# for x in myresult:
#     print(x)