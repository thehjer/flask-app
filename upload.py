import mysql.connector
mydb=mysql.connector.connect(    
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
book_list=[]
mycursor=mydb.cursor()

f=open("book.csv")
book_list=[]
for l in f:
    l=l.strip()
    l=l.split(',')
    book_list.append(l)
mycursor=mydb.cursor()
sql="INSERT INTO book(title,author,date) VALUES(%s,%s,%s)"
for book in book_list:
    mycursor.execute(sql,book)
    print(mycursor.rowcount,"record inserted")
mydb.commit()




# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# app = Flask(__name__)



# @app.route('/')
# def upload_file():
#     return render_template('upload.html')

# @app.route('/upload', methods = ['GET', 'POST'])
# def uploadfile():
#    if request.method == 'POST': 
#     f = request.files['file'] 
#     f.save(secure_filename(f.filename))
#     print(f)
#     return 'file uploaded successfully'
        
# if __name__ == '__main__':
#    app.run()