import mysql.connector
mydb=mysql.connector.connect(    
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
book_list=[]
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM book")
myresult=mycursor.fetchall()

for x in myresult:
    book_list.append(x[1:])

print(book_list)