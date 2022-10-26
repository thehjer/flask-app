import mysql.connector
mydb=mysql.connector.connect(    
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
mycursor=mydb.cursor()


sql = "DELETE FROM book WHERE author=rrr"
# adr = ("jk", )

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")